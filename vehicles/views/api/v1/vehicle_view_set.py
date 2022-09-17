from rest_framework.viewsets import ReadOnlyModelViewSet
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from rest_framework.pagination import PageNumberPagination


class VehiclesViewSet(ReadOnlyModelViewSet):
    queryset = Vehicle.objects.get_active_vehicles()
    serializer_class = VehicleSerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'options', 'head']
