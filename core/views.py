# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# django
from django.shortcuts import render
from django.http import HttpResponse


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