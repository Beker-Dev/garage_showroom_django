from django.db.models import TextChoices


class Type(TextChoices):
    CAR = 'c', 'car'
    MOTORCYCLE = 'm', 'motorcycle'
