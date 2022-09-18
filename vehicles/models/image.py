from django.db import models
from vehicles.models import Vehicle


class Image(models.Model):
    image = models.ImageField(upload_to='vehicles/images/%Y/%m/%d', blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name
