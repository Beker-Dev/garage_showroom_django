from django.views.generic import ListView
from vehicles.models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin


class List(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    redirect_field_name = 'next'
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'vehicles/home.html'
    paginate_by = 12
    ordering = ['-id']
    queryset = Vehicle.objects.get_active_vehicles()
