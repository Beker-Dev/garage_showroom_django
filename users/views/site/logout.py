from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View


class Logout(View):
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
            return redirect('users:login')
        else:
            return HttpResponse(status=401)
