from vehicles.models import Brand
from vehicles.serializers import BrandSerializer
from vehicles.views.api.v1 import BaseViewSet


class BrandViewSet(BaseViewSet):
    queryset = Brand.objects.get_active_brands()
    serializer_class = BrandSerializer
