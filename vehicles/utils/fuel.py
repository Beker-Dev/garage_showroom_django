from django.db.models import TextChoices


class Fuel(TextChoices):
    GASOLINE = 'gas', 'gasoline'
    DIESEL = 'dsl', 'diesel'
    ELECTRIC = 'elt', 'electric'
    HYBRID = 'hbd', 'hybrid'
