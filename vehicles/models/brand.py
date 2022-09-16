from vehicles.models.abstract_model import AbstractModel
from django.db import models


class Brand(AbstractModel):
    name = models.CharField(max_length=255, unique=True)
