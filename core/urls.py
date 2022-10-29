from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from . import forms

urlpatterns = [

    # api
    path('api/turbidity-records/<int:device_id>', views.api_device_record),
    path('api/turbidity-records/', views.api_records),



    # authentication
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('register-complete/', views.register_complete, name='register_complete'),
    path('', views.dashboard, name='dashboard'),


    # reset password
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='reset-password.html',
        form_class=forms.ResetPasswordForm), name='password_reset'),
        
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset-password-sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset-password-confirm.html',
        form_class=forms.ResetPasswordConfirmForm), name='password_reset_confirm'),

    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset-password-complete.html'), name='password_reset_complete'),
    


    # application
    path('turbidity-records/<int:device_id>', views.turbidity_records, name='turbidity_records'),
    path('list-devices/', views.list_devices, name='list_devices'),
    path('add-device/', views.add_device, name='add_device'),
    path('add-component/', views.add_component, name='add_component'),
    path('edit-device/<int:device_id>', views.edit_device, name='edit_device'),
    path('edit-component/<int:component_id>', views.edit_component, name='edit_component'),
    path('delete-device/<int:device_id>', views.delete_device, name='delete_device'),
    path('delete-component/<int:component_id>', views.delete_component, name='delete_component'),

    
]
