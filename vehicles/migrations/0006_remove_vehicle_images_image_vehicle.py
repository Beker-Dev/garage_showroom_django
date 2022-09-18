# Generated by Django 4.1.1 on 2022-09-18 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_rename_image_vehicle_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='vehicle',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle'),
            preserve_default=False,
        ),
    ]
