from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput({
            'placeholder': 'Type your email here',
            'class': 'form-control'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError('Invalid Email', code='invalid')
        else:
            return email
