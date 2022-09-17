# Generated by Django 4.1.1 on 2022-09-17 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_remove_vehicle_is_turbo_vehicle_engine_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicles/images/%Y/%m/%d')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ManyToManyField(to='vehicles.image'),
        ),
    ]
