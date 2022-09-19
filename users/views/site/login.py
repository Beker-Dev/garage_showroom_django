from django.views import View
from django.shortcuts import render, redirect
from users.forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


class Login(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('vehicles:list')
        else:
            form = LoginForm()
            return render(self.request, 'users/login.html', {'form': form})

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            authenticated_user = authenticate(
                username=username, password=password
            )

            if authenticated_user is not None:
                login(self.request, authenticated_user)
                return redirect('vehicles:list')

        messages.error(self.request, 'Invalid username or password')
        return redirect('users:login')
