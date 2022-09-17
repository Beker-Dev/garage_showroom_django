from django.contrib import admin
from vehicles.models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'brand',
        'is_active'
    ]
    list_display_links = [
        'id',
        'name',
        'brand'
    ]
    list_filter = ['brand']
    list_editable = ['is_active']
    list_per_page = 12
    ordering = ['-id']
