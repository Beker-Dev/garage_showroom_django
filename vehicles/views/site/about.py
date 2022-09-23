from django.views.generic import TemplateView
from django.utils.lorem_ipsum import COMMON_P


class About(TemplateView):
    template_name = 'vehicles/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lorem'] = (COMMON_P + '\n') * 10
        return context
