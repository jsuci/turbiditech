# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from core.models import Device, Component, TurbidityRecord

# forms
from . import forms



# api
@api_view(['GET'])
def get_users(request):
    person = {
        'name': 'Sam',
        'age': 33
    }
    return Response(person)


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

    detectors = Device.objects.all().values('id', 'device_name', 'location')
    

    context = {
        'box_contents': detectors
    }

    return render(request, 'dashboard.html', context)


@login_required
def turbidity_records(request, device_id):

    # use device_id to locate in db the specific entry or device

    device_record = Device.objects.filter(id=device_id).values(
        'id', 'device_name', 'turbidityrecord__id', 'turbidityrecord__record_date',
        'turbidityrecord__record_time', 'turbidityrecord__record_image',
        'turbidityrecord__valve_status', 'turbidityrecord__water_status')


    context = {
        'records': device_record
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