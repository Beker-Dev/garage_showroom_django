from django.contrib import admin
from vehicles.models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'mileage', 'price', 'year', 'is_new', 'fuel', 'engine',
                    'engine_type',  'automatic_transmission',
                    'gears', 'type'
                    ]
    list_display_links = ['id', 'model']
    list_filter = ['model__brand', 'is_new', 'fuel', 'engine', 'engine_type', 'automatic_transmission', 'type']
