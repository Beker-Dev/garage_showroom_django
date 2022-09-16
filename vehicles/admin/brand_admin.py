from django.contrib import admin
from vehicles.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ...
