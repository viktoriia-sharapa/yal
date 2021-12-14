from rest_framework import routers
from .api import DriverViewSet, VehicleViewSet

router = routers.DefaultRouter()
router.register('api/DriverVehicle', DriverViewSet, 'Driver')
router.register('api/DriverVehicle', VehicleViewSet, 'Vehicle')


urlpatterns = router.urls