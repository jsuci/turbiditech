# rest_framework
from multiprocessing import context
from rest_framework.decorators import api_view
from rest_framework.response import Response

# django
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


@api_view(['GET'])
def get_users(request):
    person = {
        'name': 'Sam',
        'age': 33
    }
    return Response(person)


def login(request):
    context = {
        'header_title': 'Log In | Turbiditech AI'
    }
    return render(request, 'login.html', context)


def logout(request):
    return render(request, 'logout.html')


def register(request):
    context = {
        'header_title': 'Register | Turbiditech AI'
    }

    return render(request, 'register.html', context)


def dashboard(request):
    context = {
        'header_title': 'Register | Turbiditech AI',
        'box_contents': [
            {
                'detector_id': 1,
                'detector_name': 'Detector 1',
                'turbidity': 'clean',
                'device_status': 'on',
                'valve_status': 'on',
                'location': 'WTP Upper Area'
            },
            {
                'detector_id': 2,
                'detector_name': 'Detector 2',
                'turbidity': 'dirty',
                'device_status': 'on',
                'valve_status': 'off',
                'location': 'WTP Lower Area'
            },
            {
                'detector_id': 3,
                'detector_name': 'Detector 3',
                'turbidity': 'clean',
                'device_status': 'on',
                'valve_status': 'on',
                'location': 'Zone 7 Linabo'
            },
            {
                'detector_id': 4,
                'detector_name': 'Detector 4',
                'turbidity': 'clean',
                'device_status': 'on',
                'valve_status': 'off',
                'location': 'Maramag, Bukidnon'
            },
            {
                'detector_id': 5,
                'detector_name': 'Detector 5',
                'turbidity': 'clean',
                'device_status': 'on',
                'valve_status': 'on',
                'location': 'Mulmac, Macabalan'
            },
        ]
    }

    return render(request, 'dashboard.html', context)


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


def list_devices(request):
    # notification message after successful form submit
    # must be placed inside if form.is_valid()
    # messages.add_message(request, messages.INFO, 'Form submitted successfully.')

    context = {
        'devices': [
            {
                'device_id': 1,
                'device_name': 'Detector 1',
                'device_status': 'active',
                'device_location': 'WTP Upper Area',
                'install_date': '10/12/2022',
                'managed_by': 'Jamil B. Magsuci'
            },
            {
                'device_id': 2,
                'device_name': 'Detector 2',
                'device_status': 'active',
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