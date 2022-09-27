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
        'header_title': 'Register | Turbiditech AI'
    }
    return render(request, 'dashboard.html', context)