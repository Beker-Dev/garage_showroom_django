# Generated by Django 4.1.1 on 2022-09-17 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_image_vehicle_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='image',
            new_name='images',
        ),
    ]