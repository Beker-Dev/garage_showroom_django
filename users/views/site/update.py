from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UpdateForm
from django.urls import reverse


class Update(LoginRequiredMixin, UpdateView):
    login_url = '/users/login/'
    redirect_field_name = 'next'
    model = User
    form_class = UpdateForm
    template_name = 'users/update.html'

    def get_object(self, *args, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse('users:detail')
