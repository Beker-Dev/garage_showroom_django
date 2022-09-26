from rest_framework import serializers
from vehicles.models import Vehicle
from .model_serializer import ModelSerializer


class VehicleSerializer(serializers.ModelSerializer):
    model = ModelSerializer()

    class Meta:
        model = Vehicle
        fields = [
            'id',
            'model',
            'color',
            'mileage',
            'price',
            'year',
            'is_new',
            'fuel',
            'engine',
            'engine_type',
            'automatic_transmission',
            'gears',
        ]
