from django.db.models import TextChoices


class Engine(TextChoices):
    I3_10 = 'I3 1.0', 'I3 1.0'
    I3_16 = 'I3 1.6', 'I3 1.6'
    I4_10 = 'I4 1.0', 'I4 1.0'
    I4_16 = 'I4 1.6', 'I4 1.6'
    I4_20 = 'I4 2.0', 'I4 2.0'
    I4_22 = 'I4 2.2', 'I4 2.2'
    I4_25 = 'I4 2.5', 'I4 2.5'
    I6_30 = 'I6 3.0', 'I6 3.0'
    V6_30 = 'V6 3.0', 'V6 3.0'
    V6_33 = 'V6 3.3', 'V6 3.3'
    V8_40 = 'V8 4.0', 'V8 4.0'
    V8_50 = 'V8 5.0', 'V8 5.0'
    V8_60 = 'V8 6.0', 'V8 6.0'
    V8_70 = 'V8 7.0', 'V8 7.0'
    V8_80 = 'V8 8.0', 'V8 8.0'
    V10 = 'V10', 'V10'
    V12 = 'V12', 'V12'
    W16 = 'W16', 'W16'
    BATTERY = 'Battery', 'Battery'
    CUSTOM = 'Custom', 'Custom'
