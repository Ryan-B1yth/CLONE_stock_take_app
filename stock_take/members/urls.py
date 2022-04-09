"""
Imports
"""
from django.urls import path
from .views import login
from .views import UserRegisterView

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
]