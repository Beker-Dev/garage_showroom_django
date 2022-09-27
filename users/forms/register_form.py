from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
        required_length = 8
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_space = False
        if len(password) < required_length:
            raise ValidationError(f'Password must have at least {required_length} characters', code='min_length')
        else:
            for c in password:
                if c.islower():
                    has_lowercase = True
                if c.isupper():
                    has_uppercase = True
                if c.isdigit():
                    has_digit = True
                if c.isspace():
                    has_space = True
            else:
                if not has_lowercase or not has_uppercase or not has_digit or has_space:
                    raise ValidationError(
                            f'Password must have at least one lowercase, uppercase, digit and no '
                            f'spaces', code='invalid'
                        )
                else:
                    return password

    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get('password')
        pw2 = cleaned_data.get('password2')
        pw_error = 'Password must be equal'
        if pw != pw2:
            raise ValidationError({'password': pw_error, 'password2': pw_error})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

