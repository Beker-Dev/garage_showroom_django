from django.db.models import TextChoices


class Color(TextChoices):
    RED = 'Red', 'Red'
    GREEN = 'Green', 'Green'
    BLUE = 'Blue', 'Blue'
    BLACK = 'Black', 'Black'
    WHITE = 'White', 'White'
    YELLOW = 'Yellow', 'Yellow'
    GREY = 'Grey', 'Grey'
    PINK = 'Pink', 'Pink'
    ORANGE = 'Orange', 'Orange'
    CHROME = 'Chrome', 'Chrome'
    CUSTOM = 'Custom', 'Custom'
