from rest_framework import serializers
from core.models import Device, TurbidityRecord, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'profile_image']


class DeviceRecordSerializer(serializers.ModelSerializer):


    device_name = serializers.SerializerMethodField('get_device_name')

    class Meta:
        model = TurbidityRecord
        fields = [
            'valve_status', 'water_status', 'record_image',
            'record_device', 'details', 'created_on', 'device_name', 'id'
        ]

    def get_device_name(self, obj):
        return obj.record_device.device_name


class AllRecordSerializer(serializers.ModelSerializer):
    records = DeviceRecordSerializer(many=True)

    class Meta:
        model = Device
        fields = [
            'id', 'device_name', 'location', 'records'
        ]