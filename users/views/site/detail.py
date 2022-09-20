from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import redirect


class Detail(DetailView):
    model = User
    template_name = 'users/detail.html'
    context_object_name = 'user'

    def dispatch(self, *args, **kwargs):
        if self.kwargs.get('pk') != self.request.user.pk:
            return redirect('vehicles:list')
        return super().dispatch(*args, **kwargs)
