# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from django.urls import is_valid_path, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# forms
from .forms import LoginForm, RegisterForm



# api
@api_view(['GET'])
def get_users(request):
    person = {
        'name': 'Sam',
        'age': 33
    }
    return Response(person)


def user_login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            # Redirect to dashboard
            return redirect('dashboard') 
        else:
            # Return an 'invalid login' error message.
            messages.add_message(request, messages.INFO, 'Incorrect email or password.')


    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('dashboard')


def register(request):
    form = RegisterForm()
    
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user_login')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


@login_required
def dashboard(request):
    context = {
        'header_title': 'Register | Turbiditech AI',
        'box_contents': [
            {
                'detector_id': 1,
                'detector_name': 'Detector 1',
                'turbidity': 'clean',
                'device_status': 'online',
                'valve_status': 'on',
                'location': 'WTP Upper Area'
            },
            {
                'detector_id': 2,
                'detector_name': 'Detector 2',
                'turbidity': 'dirty',
                'device_status': 'online',
                'valve_status': 'off',
                'location': 'WTP Lower Area'
            },
            {
                'detector_id': 3,
                'detector_name': 'Detector 3',
                'turbidity': 'clean',
                'device_status': 'online',
                'valve_status': 'on',
                'location': 'Zone 7 Linabo'
            },
            {
                'detector_id': 4,
                'detector_name': 'Detector 4',
                'turbidity': 'clean',
                'device_status': 'online',
                'valve_status': 'off',
                'location': 'Maramag, Bukidnon'
            },
            {
                'detector_id': 5,
                'detector_name': 'Detector 5',
                'turbidity': 'dirty',
                'device_status': 'offline',
                'valve_status': 'on',
                'location': 'Mulmac, Macabalan'
            },
        ]
    }

    return render(request, 'dashboard.html', context)


@login_required
def turbidity_records(request, device_id):

    # use device_id to locate in db the specific entry or device
    
    context = {
        'device_name': 'Detector 1',
        'records': [
            {
                'capture_id': 1,
                'capture_date': '10/12/2022',
                'capture_time': '10:42 AM',
                'image_link': 'https://turbiditech.fly.dev/captured/img_20221010.jpg',
                'valve_status': 'off',
                'turbidity_status': 'dirty',
            },
            {
                'capture_id': 2,
                'capture_date': '10/12/2022',
                'capture_time': '10:42 AM',
                'image_link': 'https://turbiditech.fly.dev/captured/img_20221010.jpg',
                'valve_status': 'on',
                'turbidity_status': 'clean',
            }
        ]
    }

    return render(request, 'turbidity-records.html', context)


@login_required
def list_devices(request):
    # notification message after successful form submit
    # must be placed inside if form.is_valid()
    # messages.add_message(request, messages.INFO, 'Form submitted successfully.')

    context = {
        'devices': [
            {
                'device_id': 1,
                'device_name': 'Detector 1',
                'device_status': 'online',
                'device_location': 'WTP Upper Area',
                'install_date': '10/12/2022',
                'managed_by': 'Jamil B. Magsuci'
            },
            {
                'device_id': 2,
                'device_name': 'Detector 2',
                'device_status': 'online',
                'device_location': 'Zone 7 Linabo',
                'install_date': '10/25/2022',
                'managed_by': 'Jamil B. Magsuci'
            }
        ],
        'components': [
            {
                'component_id': 1,
                'component_name': 'Camera Module',
                'device_linked': 'Detector 1',
                'install_date': '10/25/2022',
                'managed_by': 'Jamil B. Magsuci'
            },
            {
                'component_id': 2,
                'component_name': 'Solenoid Valve',
                'device_linked': 'Detector 2',
                'install_date': '10/25/2022',
                'managed_by': 'Jamil B. Magsuci'
            }
        ]
    }

    return render(request, 'list-devices.html', context)


@login_required
def add_device(request):
  template = loader.get_template('add-device.html')
  return HttpResponse(template.render({}, request))


@login_required
def edit_device(request, device_id):
  template = loader.get_template('edit-device.html')
  return HttpResponse(template.render({}, request))


@login_required
def add_component(request):
  template = loader.get_template('add-component.html')
  return HttpResponse(template.render({}, request))


@login_required
def edit_component(request, component_id):
  template = loader.get_template('edit-component.html')
  return HttpResponse(template.render({}, request))