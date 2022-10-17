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
    path('add-device/', views.add_device, name='add_device'),
    path('edit-device/<int:device_id>', views.edit_device, name='edit_device'),
    path('add-component/', views.add_component, name='add_component'),
    path('edit-component/<int:component_id>', views.edit_component, name='edit_component'),
]
