from django.views.generic import ListView
from vehicles.models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.exceptions import FieldError


class List(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'vehicles/home.html'
    paginate_by = 4
    ordering = ['-id']
    queryset = Vehicle.objects.get_active_vehicles()

    def check_filters(self):
        allowed_filters = ['type']
        for filter, value in self.request.GET.items():
            if filter in allowed_filters and value:
                try:
                    self.queryset = self.queryset.filter(**{filter: value})
                except FieldError:
                    filter = f'model__{filter}'
                    self.queryset = self.queryset.filter(**{filter: value})
        return self.queryset

    def check_search(self):
        search = self.request.GET.get('search')
        if search is not None:
            self.queryset = self.queryset.filter(
                Q(color__icontains=search) |
                Q(model__name__icontains=search) |
                Q(model__brand__name__icontains=search) |
                Q(price__icontains=search) |
                Q(year__icontains=search) |
                Q(fuel__icontains=search)
            )
        return self.queryset

    def get_queryset(self):
        self.check_filters()
        self.check_search()
        return super().get_queryset()
