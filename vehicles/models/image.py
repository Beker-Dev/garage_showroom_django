from django.db import models
from vehicles.models import Vehicle
from vehicles.utils.functions import resize_image, remove_image


class Image(models.Model):
    image = models.ImageField(upload_to='vehicles/images/%Y/%m/%d', blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name

    def __update(self):
        if self.id is not None:
            old_image = Image.objects.get(id=self.id)
            if self.image != old_image.image:
                remove_image(old_image.image)

    def save(self, *args, **kwargs):
        self.__update()
        super().save(*args, **kwargs)
        if self.image:
            resize_image(self.image)

    def delete(self, *args, **kwargs):
        remove_image(self.image)
        super().delete(*args, **kwargs)
