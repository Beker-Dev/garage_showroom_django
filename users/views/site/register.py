from django.views.generic import CreateView
from django.contrib.auth.models import User
from users.forms import RegisterForm
from django.shortcuts import redirect


class Register(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('vehicles:list')
        else:
            return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)  # encrypt password
        return super().form_valid(form)
