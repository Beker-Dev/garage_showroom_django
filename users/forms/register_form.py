from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from users.utils.form_utils import *


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control'
            }
        )
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email@example.com',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'form-control'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        required_length = 6
        if len(username) < required_length:
            raise ValidationError(f'Username must have at least {required_length} characters', code='min_length')
        return username

    def clean_password(self):
        password = str(self.cleaned_data.get('password'))
        return validate_password(password)

    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get('password')
        pw2 = cleaned_data.get('password2')
        return compare_passwords(pw, pw2)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

