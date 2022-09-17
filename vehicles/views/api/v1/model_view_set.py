from vehicles.models import Model
from vehicles.serializers import ModelSerializer
from vehicles.views.api.v1 import BaseViewSet


class ModelViewSet(BaseViewSet):
    queryset = Model.objects.get_active_models()
    serializer_class = ModelSerializer

