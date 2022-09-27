from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(pre_save, sender=User)
def pre_save_user(instance, **kwargs):
    instance.first_name = instance.first_name.title()
    instance.last_name = instance.last_name.title()

