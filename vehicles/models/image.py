from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='vehicles/images/%Y/%m/%d', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)
