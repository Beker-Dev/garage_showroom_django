from rest_framework import serializers
from vehicles.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name'
        ]
