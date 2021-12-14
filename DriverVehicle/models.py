from django.db import models
from django.utils import timezone

# Create your models here.


class Driver(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{self.first_name} {self.last_name}'


class Vehicle(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
