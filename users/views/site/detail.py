from django.views.generic import DetailView
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm


class Detail(DetailView):
    slug_url_kwarg = 'username'
    slug_field = 'username'
    model = User
    template_name = 'users/detail.html'
    context_object_name = 'user'
