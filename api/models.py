from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN' , 'Admin'
        DRIVER = 'driver', 'Driver'
        PASSENGER = 'passenger', 'Passenger'
    user_type = models.CharField(max_length=20, choices=Role.choices)
    
class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)      

class Location(models.Model):
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    

class Bus(models.Model):
    busno = models.IntegerField(unique=True)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

class RoutesName(models.Model):
    route_name = models.CharField(max_length=100)

class Routes(models.Model):
    route = models.IntegerField()
    route_name = models.CharField(max_length=100)
    order = models.IntegerField()
    bus_id = models.IntegerField(null=True,default=None)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)




