from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Device

admin.site.register(CustomUser)
# admin.site.register(Device)