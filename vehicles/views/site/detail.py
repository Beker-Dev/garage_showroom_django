from django.views.generic import DetailView
from vehicles.models import Vehicle


class Detail(DetailView):
    model = Vehicle
    template_name = 'vehicles/detail.html'
    context_object_name = 'vehicle'
