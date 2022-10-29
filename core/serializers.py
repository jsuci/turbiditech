from rest_framework import serializers
from core.models import Device, TurbidityRecord

class DeviceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurbidityRecord
        fields = [
            'valve_status', 'water_status', 'record_image',
            'record_device', 'details', 'created_on'
        ]


class RecordSerializer(serializers.ModelSerializer):
    record_device = DeviceRecordSerializer(many=True)
    class Meta:
        model = Device
        fields = [
            'id', 'device_name', 'location', 'record_device'
        ]