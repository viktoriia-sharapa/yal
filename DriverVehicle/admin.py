from django.contrib import admin
from .models import Driver, Vehicle

# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name')


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at')
    list_display_links = ('id', 'driver_id', 'make', 'model', 'plate_number')
    list_display_links = ('id', 'driver_id', 'make', 'model', 'plate_number')


admin.site.register(Driver, DriverAdmin)
admin.site.register(Vehicle, VehicleAdmin)
