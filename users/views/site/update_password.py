from django.views.generic import FormView
from users.forms import UpdatePasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect


class UpdatePassword(LoginRequiredMixin, FormView):
    login_url = '/users/login/'
    redirect_field_name = 'next'
    template_name = 'users/update_password.html'
    success_url = '/users/login/'
    form_class = UpdatePasswordForm

    def form_valid(self, form):
        password = form.data.get('password')
        if self.request.user.check_password(password):
            new_password = form.data.get('new_password')
            self.request.user.set_password(new_password)
            self.request.user.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
