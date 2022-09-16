from vehicles.models import AbstractModel
from vehicles.utils.color import Color
from vehicles.utils.fuel import Fuel
from vehicles.utils.type import Type
from vehicles.utils.engine import Engine
from vehicles.models import Model
from django.db import models


class Vehicle(AbstractModel):
    color = models.CharField(max_length=255, choices=Color.choices, default=Color.BLACK)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    mileage = models.FloatField(default=0)
    price = models.FloatField(default=0)
    year = models.IntegerField()
    is_new = models.BooleanField(default=True)
    fuel = models.CharField(max_length=255, choices=Fuel.choices, default=Fuel.GASOLINE)
    engine = models.CharField(max_length=255, choices=Engine.choices, default=Engine.I3_10)
    is_turbo = models.BooleanField(default=False)
    gears = models.IntegerField()
    automatic_transmission = models.BooleanField(default=False)
    type = models.CharField(max_length=255, choices=Type.choices, default=Type.CAR)

    def __str__(self):
        return self.model.name
