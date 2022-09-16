from django.contrib import admin
from vehicles.models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    ...
