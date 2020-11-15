from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    # path('', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('index/', IndexView.as_view(), name='index'),

    path('account/create', UserCreateView.as_view(), name='user_create'),
]
