from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class BaseViewSet(ReadOnlyModelViewSet):
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'options', 'head']
    permission_classes = [IsAuthenticated]
