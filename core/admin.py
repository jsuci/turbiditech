from django.contrib import admin
from .models import CustomUser, Device, Component, TurbidityRecord, AdminUpdate

admin.site.register(CustomUser)
admin.site.register(Device)
admin.site.register(Component)
admin.site.register(TurbidityRecord)
admin.site.register(AdminUpdate)