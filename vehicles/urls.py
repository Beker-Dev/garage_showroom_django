from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

app_name = 'vehicles'

router = SimpleRouter()
router.register('api/v1/brands', views.api.BrandViewSet, basename='api-v1-brands')
router.register('api/v1/models', views.api.ModelViewSet, basename='api-v1-models')
router.register('api/v1', views.api.VehiclesViewSet, basename='api-v1')

urlpatterns = [
    path('home/', views.site.List.as_view(), name='list'),
]

urlpatterns += router.urls
