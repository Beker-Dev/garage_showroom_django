from django.db.models import TextChoices


class EngineType(TextChoices):
    ASPIRATED = 'Aspirated', 'Aspirated'
    TURBO = 'Turbo', 'Turbo'
    BITURBO = 'Biturbo', 'Biturbo'
    QUADTURBO = 'Quadturbo', 'Quadturbo'
    SUPERCHARGED = 'Supercharged', 'Supercharged'
