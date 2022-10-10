from django import forms
from users.utils.form_utils import *


class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )

    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'New Password',
                'class': 'form-control'
            }
        )
    )

    new_password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm New Password',
                'class': 'form-control'
            }
        )
    )

    def clean(self):
        password = self.cleaned_data.get('password')
        new_password = self.cleaned_data.get('new_password')
        new_password_confirm = self.cleaned_data.get('new_password_confirm')
        validate_password(new_password)
        compare_passwords(new_password, new_password_confirm)
        if password == new_password:
            raise ValidationError(
                'Password and New Password cannot be equal', code='invalid'
            )
