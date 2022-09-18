from django.contrib import admin
from vehicles.models import Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1
    fields = ['image']
