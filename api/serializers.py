from .models import Driver,Bus,Routes
from rest_framework import serializers


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'
