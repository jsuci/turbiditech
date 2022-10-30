# rest_framework
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Device, Component, TurbidityRecord
from django.views.decorators.csrf import csrf_exempt

# forms
from . import forms

# serializers
from core.serializers import DeviceRecordSerializer, RecordSerializer



# api
@api_view(['GET', 'PUT'])
@csrf_exempt
def api_device_record(request, device_id):
    try:
        device_records = TurbidityRecord.objects.filter(record_device=device_id)
    except TurbidityRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeviceRecordSerializer(device_records, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeviceRecordSerializer(data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def api_records(request):
    try:
        all_records = Device.objects.all()
    except TurbidityRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecordSerializer(all_records, many=True)
        return Response(serializer.data)


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

    csrf = request.META['CSRF_COOKIE']
  

    context = {
        'csrf': csrf
    }

    return render(request, 'dashboard.html', context)


@login_required
def turbidity_records(request, device_id):

    # use device_id to locate in db the specific entry or device

    records = Device.objects.filter(id=device_id).values(
        'device_name', 'records__id', 'records__record_date',
        'records__record_time', 'records__record_image',
        'records__valve_status', 'records__water_status',
        'records__details')

    context = {
        'records': records
    }

    return render(request, 'turbidity-records.html', context)


@login_required
def list_devices(request):
    # notification message after successful form submit
    # must be placed inside if form.is_valid()
    # messages.add_message(request, messages.INFO, 'Form submitted successfully.')

    devices = Device.objects.all()
    components = Component.objects.all()

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
            form.save()
            return redirect('list_devices')

    context = {
        'form': form
    }

    return render(request, 'add-device.html', context)


@login_required
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
def delete_device(request, device_id):
    selected_device = Device.objects.get(id=device_id)
    selected_device.delete()
    
    return redirect('list_devices')


@login_required
def delete_component(request, component_id):
    selected_component = Component.objects.get(id=component_id)
    selected_component.delete()
    
    return redirect('list_devices')