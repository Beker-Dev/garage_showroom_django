from django.views.generic import ListView
from vehicles.models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin


class List(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'vehicles/home.html'
    paginate_by = 20
    ordering = ['-id']
    queryset = Vehicle.objects.get_active_vehicles()
