# Generated by Django 4.1.1 on 2022-09-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0006_remove_vehicle_images_image_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='description',
            field=models.TextField(default='...'),
            preserve_default=False,
        ),
    ]
