from django.contrib import admin
from vehicles.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'is_active'
    ]
    list_display_links = [
        'id',
        'name'
    ]
    list_editable = ['is_active']
    list_per_page = 12
    ordering = ['-id']
