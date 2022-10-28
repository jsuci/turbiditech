from rest_framework import serializers
from core.models import TurbidityRecord


class TurbidityRecordSerializer(serializers.ModelSerializer):
    device_name = serializers.ReadOnlyField(source='record_device.device_name')
    device_id = serializers.ReadOnlyField(source='record_device.id')
    location = serializers.ReadOnlyField(source='record_device.location')
    
    class Meta:
        model = TurbidityRecord
        fields = [
            'device_name', 'device_id', 'location',
            'valve_status', 'water_status', 'record_image',
            'record_device', 'details'
        ]