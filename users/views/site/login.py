from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import LoginForm
from django.contrib.auth import login, authenticate


class Login(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(self.request, 'vehicles/home.html')
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
                return HttpResponse(f"logged as: {self.request.user}")

        print('no')
        return redirect('users:login')
