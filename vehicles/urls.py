from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

app_name = 'vehicles'

router = SimpleRouter()
router.register('vehicles/api/v1/brands', views.api.BrandViewSet, basename='api-v1-brands')
router.register('vehicles/api/v1/models', views.api.ModelViewSet, basename='api-v1-models')
router.register('vehicles/api/v1', views.api.VehiclesViewSet, basename='api-v1')

urlpatterns = [
    path('', views.site.redirect_to_home, name='redirect-to-home'),
    path('vehicles/home/', views.site.List.as_view(), name='list'),
    path('vehicles/detail/<int:pk>', views.site.Detail.as_view(), name='detail'),
    path('about/', views.site.About.as_view(), name='about'),
]

urlpatterns += router.urls
