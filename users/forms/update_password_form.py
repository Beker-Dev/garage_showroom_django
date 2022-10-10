from django import forms


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
