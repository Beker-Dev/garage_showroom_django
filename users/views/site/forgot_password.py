from django.views.generic import FormView
from users.forms import ForgotPasswordForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
import string
import random
from django.contrib import messages
import smtplib
from users.utils.email_utils import EMAIL, PASSWORD


class ForgotPassword(FormView):
    form_class = ForgotPasswordForm
    template_name = 'users/forgot_password.html'
    success_url = '/users/login/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('users:detail')
        return super().dispatch(*args, **kwargs)

    @staticmethod
    def get_user(email: str):
        return User.objects.filter(email=email).first()

    @staticmethod
    def get_new_pw():
        return ''.join(
            random.sample(
                string.ascii_letters + string.digits + string.punctuation,
                20
            )
        )

    @staticmethod
    def send_email(msg: str, user: User):
        with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(user=EMAIL, password=PASSWORD)
            smtp.sendmail(EMAIL, user.email, msg)

    def form_valid(self, form):
        user = self.get_user(form.data.get('email'))
        if user:
            new_pw = self.get_new_pw()
            message = f"""\
            Subject: Hi there

            This is your new password: {new_pw}"""
            user.set_password(new_pw)
            user.save()
            self.send_email(message, user)
            messages.info(self.request, 'Email sent with password information!')
            return redirect('users:login')
        else:
            messages.error(self.request, 'Email not found!')
            return super().form_invalid(form)
