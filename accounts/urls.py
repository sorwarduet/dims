from django.urls import path
from .views import UserLoginView, IndexView

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('index/', IndexView.as_view(), name='index')
]
