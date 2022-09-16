from django.db.models import TextChoices


class Fuel(TextChoices):
    GASOLINE = 'Gasoline', 'Gasoline'
    DIESEL = 'Diesel', 'Diesel'
    ELECTRIC = 'Electric', 'Electric'
    HYBRID = 'Hybrid', 'Hybrid'
