from vehicles.models.abstract_model import AbstractModel
from vehicles.models import Brand
from django.db import models


class Model(AbstractModel):
    name = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
