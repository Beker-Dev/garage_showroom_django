from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Vehicle
from vehicles.utils.functions import remove_image


@receiver(pre_delete, sender=Vehicle)
def pre_delete_vehicle(instance, **kwargs):
    for img in instance.image_set.all():
        remove_image(img.image)
