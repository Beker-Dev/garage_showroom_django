from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Vehicle
from vehicles.utils.functions import *


@receiver(pre_save, sender=Vehicle)
def pre_save_vehicle(instance, **kwargs):
    old_imgs = None
    try:
        old_imgs = Vehicle.objects.filter(pk=instance.id).first().image_set.all()
        new_imgs = instance.image_set.all()

        if old_imgs != new_imgs:
            for img in new_imgs:
                resize_image(img.image)
    except Exception:
        ...


@receiver(pre_delete, sender=Vehicle)
def pre_delete_vehicle(instance, **kwargs):
    for img in instance.image_set.all():
        remove_image(img.image)
