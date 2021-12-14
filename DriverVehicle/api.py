from .models import Driver, Vehicle
from rest_framework import viewsets, permissions
from .serializers import DriverSerializer, VehicleSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = DriverSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VehicleSerializer
