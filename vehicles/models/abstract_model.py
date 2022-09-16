from django.db import models
from vehicles.managers import AbstractModelManager


class AbstractModel(models.Model):
    objects = AbstractModelManager()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
