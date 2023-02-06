from django.contrib import admin
from .models import CustomUser, Device, Component, TurbidityRecord

admin.site.register(CustomUser)
admin.site.register(Device)
admin.site.register(Component)
admin.site.register(TurbidityRecord)
