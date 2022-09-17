import rest_framework.pagination
from django.contrib import admin
from vehicles.models import Vehicle
from vehicles.admin import ImageInline


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'model',
        'mileage',
        'price',
        'year',
        'is_new',
        'fuel',
        'engine',
        'engine_type',
        'automatic_transmission',
        'gears',
        'type',
        'is_active'
    ]
    list_display_links = [
        'id',
        'model'
    ]
    list_filter = [
        'model',
        'model__brand',
        'is_new',
        'fuel',
        'engine',
        'engine_type',
        'automatic_transmission',
        'type',
        'is_active'
    ]
    list_editable = ['is_active']
    list_per_page = 12
    ordering = ['-id']
    inlines = [ImageInline]
    exclude = ['images']
