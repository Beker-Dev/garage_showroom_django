from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from vehicles.views.api.v1 import BaseViewSet


class VehiclesViewSet(BaseViewSet):
    queryset = Vehicle.objects.get_active_vehicles()
    serializer_class = VehicleSerializer

