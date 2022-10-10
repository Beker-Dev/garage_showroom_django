from django.views.generic import FormView
from users.forms import UpdatePasswordForm


class UpdatePassword(FormView):
    template_name = 'users/update_password.html'
    success_url = 'users/login'
    form_class = UpdatePasswordForm
