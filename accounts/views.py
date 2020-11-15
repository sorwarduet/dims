from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import AccountAuthenticationForm, UserForm

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class UserLoginView(LoginView):
    # template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        context = {}

        user = request.user

        form = AccountAuthenticationForm()
        context['login_form'] = form

        # print(form)
        return render(request, "account/login.html", context)

    def post(self, request, *args, **kwargs):
        form = AccountAuthenticationForm(request.POST)
        context = {}
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("index")

        context['login_form'] = form

        # print(form)
        return render(request, "account/login.html", context)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class UserCreateView(LoginRequiredMixin, CreateView):
    template_name = 'account/user_add.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('employee_list')