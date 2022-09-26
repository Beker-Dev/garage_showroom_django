from django.contrib import admin
from vehicles.models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'type',
        'brand',
        'is_active'
    ]
    list_display_links = [
        'id',
        'name',
        'type',
        'brand'
    ]
    list_filter = ['brand', 'type']
    list_editable = ['is_active']
    list_per_page = 12
    ordering = ['-id']
