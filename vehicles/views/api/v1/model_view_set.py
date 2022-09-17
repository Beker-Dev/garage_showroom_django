from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from vehicles.models import Model
from vehicles.serializers import ModelSerializer


class ModelViewSet(ReadOnlyModelViewSet):
    queryset = Model.objects.get_active_models()
    serializer_class = ModelSerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'options', 'head']
