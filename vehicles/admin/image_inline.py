from django.contrib import admin
from vehicles.models import Vehicle


class ImageInline(admin.TabularInline):
    model = Vehicle.images.through
    extra = 1
    fields = ['image']
