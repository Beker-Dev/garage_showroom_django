from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class Detail(LoginRequiredMixin, DetailView):
    login_url = '/users/login/'
    redirect_field_name = 'next'
    model = User
    template_name = 'users/detail.html'
    context_object_name = 'user'

    def get_object(self, *args, **kwargs):
        return self.request.user
