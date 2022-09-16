from django.db.models import TextChoices


class Type(TextChoices):
    CAR = 'Car', 'Car'
    MOTORCYCLE = 'Motorcycle', 'Motorcycle'
