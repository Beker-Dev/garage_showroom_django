from django.views.generic import CreateView
from django.contrib.auth.models import User
from users.forms import RegisterForm


class Register(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)  # encrypt password
        return super().form_valid(form)
