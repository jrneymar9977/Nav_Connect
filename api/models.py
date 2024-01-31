from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN' , 'Admin'
        DRIVER = 'driver', 'Driver'
        TEACHER = 'passenger', 'Passenger'
    user_type = models.CharField(max_length=20, choices=Role.choices)
    
class Driver(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    user_type = UserProfile.Role.DRIVER

    def __str__(self):
        return f"{self.name} (Driver)"       
    
class Bus(models.Model):
    busno = models.IntegerField(unique=True)
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)

class Routes(models.Model):
    route_name = models.CharField(max_length=100)
    order = models.IntegerField()
    buses = models.ManyToManyField(Bus) 
