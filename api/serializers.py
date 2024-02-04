from .models import Driver,Bus,Routes,Location,User
from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['password','first_name','last_name','email','username','user_type']
#     def create(self, validated_data):
#         # Create User instances
#         user = User.objects.create_user(**validated_data)
#         return user

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['name', 'phone_number', 'user']

    def create(self, validated_data):
        driver = Driver.objects.create(**validated_data)
        return driver

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class RouteDetailSerializer(serializers.Serializer):
    route_name = serializers.CharField()
    order = serializers.IntegerField()
    lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    lang = serializers.DecimalField(max_digits=9, decimal_places=6)

class BusCreationSerializer(serializers.Serializer):
    bus_no = serializers.IntegerField()
    driver_id = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all())
    routes = RouteDetailSerializer(many=True)

