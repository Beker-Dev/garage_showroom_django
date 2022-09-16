from rest_framework.serializers import ModelSerializer
from vehicles.models import Vehicle


class VehicleSerializer(ModelSerializer):
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
            'automatic_transmission',
            'gears',
            'type'
        ]
