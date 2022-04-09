"""
Imports
"""
from django.shortcuts import render
from django.views import generic
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm


def login(request):
    """
    Login page
    """
    return render(request, 'login.html', {})


class UserRegisterView(generic.CreateView):
    """
    Register page
    """
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
