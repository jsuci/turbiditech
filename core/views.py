# rest_framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser


# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Device, Component, TurbidityRecord, CustomUser
from django.views.decorators.csrf import csrf_exempt
from core.decorators import device_user_only, component_user_only
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from datetime import datetime

# forms
from . import forms

# serializers
from core.serializers import (
    DeviceRecordSerializer,
    AllRecordSerializer,
    CustomUserSerializer,
)



# api
@api_view(['GET', 'POST'])
@csrf_exempt
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticated])
@device_user_only
def api_device_records(request, device_id):

    try:
        device_records = TurbidityRecord.objects.filter(record_device=device_id)

    except TurbidityRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeviceRecordSerializer(device_records, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeviceRecordSerializer(data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def api_all_records(request):

    try:
        all_records = Device.objects.filter(managed_by_id=request.user.id)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AllRecordSerializer(all_records, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PATCH'])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticated])
def api_users(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PATCH':
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
  
        if serializer.is_valid():
            user.profile_image.delete(save=False)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# application
def user_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard') 

    form = forms.LoginForm()
    
    if request.method == 'POST':
        email       = request.POST['email']
        password    = request.POST['password']
        user        = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('user_login')
    
    context = {
        'form': form
    }

    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('dashboard')


def register(request):
    form = forms.RegisterForm()
    
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('register_complete')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def register_complete(request):
    return render(request, 'register-complete.html', {})


@login_required
def dashboard(request):

    return render(request, 'dashboard.html', {})


@login_required
@device_user_only
def device_records(request, device_id):

    try:
        records_list = TurbidityRecord.objects.filter(record_device=device_id).values(
            'id', 'record_device', 'record_date',
            'record_time', 'record_image', 'valve_status',
            'water_status', 'details', 'created_on',
            'record_device__device_name').order_by('-id')

    except TurbidityRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




    if request.method == 'POST':

        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        if start_date <= end_date:
            filtered_results = TurbidityRecord.objects.filter(
                    record_device=device_id, record_date__range=[start_date, end_date])
            last_record = filtered_results.order_by('id').last()
            all_filtered_records = filtered_results.exclude(id=last_record.id)

            all_filtered_records.delete()

        else:
            messages.info(request, 'Invalid start and end date.')


    # paginator accepts a queryset obj and the
    # number of pages to be displayed
    # recalculate number of records
    page = request.GET.get('page', 1)
    paginator = Paginator(records_list, per_page=7)


    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    records.adjusted_elided_pages = paginator.get_elided_page_range(page, on_each_side=1)


    context = {
        'records': records
    }

    return render(request, 'device-records.html', context)

        
@login_required
def list_devices(request):
    # notification message after successful form submit
    # must be placed inside if form.is_valid()
    # messages.add_message(request, messages.INFO, 'Form submitted successfully.')

    devices = Device.objects.filter(managed_by_id=request.user.id)
    components = Component.objects.filter(device_link__managed_by_id=request.user.id)

    context = {
        'devices': devices,
        'components': components
    }

    return render(request, 'list-devices.html', context)


@login_required
def add_device(request):

    form = forms.AddDeviceForm()
    
    if request.method == 'POST':
        form = forms.AddDeviceForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.managed_by_id = request.user.id
            obj.save()
            return redirect('list_devices')

    context = {
        'form': form
    }

    return render(request, 'add-device.html', context)


@login_required
def add_component(request):
    form = forms.AddComponentForm()
    
    if request.method == 'POST':
        form = forms.AddComponentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list_devices')

    context = {
        'form': form
    }

    return render(request, 'add-component.html', context)


@login_required
@device_user_only
def edit_device(request, device_id):
    selected_device = Device.objects.get(id=device_id)

    if request.method == 'POST':
        form = forms.AddDeviceForm(request.POST, instance=selected_device)

        if form.is_valid():
            form.save()
            return redirect('list_devices')

    form = forms.AddDeviceForm(instance=selected_device)

    context = {
        'form': form
    }

    return render(request, 'edit-device.html', context)


@login_required
@component_user_only
def edit_component(request, component_id):
    selected_component = Component.objects.get(id=component_id)

    if request.method == 'POST':
        form = forms.AddComponentForm(request.POST, instance=selected_component)

        if form.is_valid():
            form.save()
            return redirect('list_devices')

    form = forms.AddComponentForm(instance=selected_component)

    context = {
        'form': form
    }

    return render(request, 'edit-component.html', context)


@login_required
@device_user_only
def delete_device(request, device_id):
    selected_device = Device.objects.get(id=device_id)
    selected_device.delete()
    
    return redirect('list_devices')


@login_required
@component_user_only
def delete_component(request, component_id):
    selected_component = Component.objects.get(id=component_id)
    selected_component.delete()
    
    return redirect('list_devices')

