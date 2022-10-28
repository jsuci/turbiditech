from rest_framework import serializers
from core.models import TurbidityRecord


class TurbidityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurbidityRecord
        fields = "__all__"