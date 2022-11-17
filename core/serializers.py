from rest_framework import serializers
from core.models import Device, TurbidityRecord, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'profile_image']


class DeviceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurbidityRecord
        fields = [
            'valve_status', 'water_status', 'record_image',
            'record_device', 'details', 'created_on'
        ]


class RecordSerializer(serializers.ModelSerializer):
    records = DeviceRecordSerializer(many=True)

    class Meta:
        model = Device
        fields = [
            'id', 'device_name', 'location', 'records'
        ]