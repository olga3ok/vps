from rest_framework import serializers
from .models import VPS


class VPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = '__all__'
        read_only_fields = ['uid']