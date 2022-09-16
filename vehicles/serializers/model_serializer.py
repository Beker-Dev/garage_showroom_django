from rest_framework import serializers
from vehicles.models import Model
from .brand_serializer import BrandSerializer


class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Model
        fields = [
            'id',
            'name',
            'brand'
        ]
