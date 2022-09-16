from django.db.models import TextChoices


class Color(TextChoices):
    RED = 'red', 'red'
    GREEN = 'grn', 'green'
    BLUE = 'blu', 'blue'
    BLACK = 'blk', 'black'
    WHITE = 'wht', 'white'
    YELLOW = 'ylw', 'yellow'
    GREY = 'gry', 'grey'
    PINK = 'pnk', 'pink'
    ORANGE = 'org', 'orange'
    CHROME = 'chm', 'chrome'
    CUSTOM = 'ctm', 'custom'
