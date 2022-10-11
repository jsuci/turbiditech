from django.urls import include, path
from . import views

urlpatterns = [
    path('api/users/', views.get_users),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('turbidity-records/<int:device_id>', views.turbidity_records, name='turbidity_records'),
    path('list-devices/', views.list_devices, name='list_devices'),
]
