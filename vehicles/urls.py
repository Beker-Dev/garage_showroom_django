from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

app_name = 'vehicles'

router = SimpleRouter()
router.register('api/v1', views.api.VehiclesViewSet, basename='api-v1')

urlpatterns = router.urls
