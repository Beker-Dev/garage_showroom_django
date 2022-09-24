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

    def check_filters(self):
        allowed_filters = ['type']
        for filter, value in self.request.GET.items():
            if filter in allowed_filters:
                self.queryset = self.queryset.filter(**{filter: value})
        return self.queryset

    def get_queryset(self):
        qs = self.check_filters()
        return qs
