from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'account/login.html'


class IndexView(TemplateView):
    template_name = 'index.html'
