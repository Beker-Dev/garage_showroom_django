from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from vehicles.models import Brand
from vehicles.serializers import BrandSerializer


class BrandViewSet(ReadOnlyModelViewSet):
    queryset = Brand.objects.get_active_brands()
    serializer_class = BrandSerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'options', 'head']
