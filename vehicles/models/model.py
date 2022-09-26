from vehicles.models.abstract_model import AbstractModel
from vehicles.models import Brand
from django.db import models
from vehicles.utils.type import Type


class Model(AbstractModel):
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255, choices=Type.choices, default=Type.CAR)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
