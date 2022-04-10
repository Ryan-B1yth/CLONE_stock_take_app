"""
Imports
"""
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.views import PasswordChangeView


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


class UserEditView(generic.UpdateView):
    """
    Edit user information
    """
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    

class ChangePasswordView(PasswordChangeView):
    """
    Change user password
    """
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_reset_success')


def password_reset_success(request):
    return render(request, 'registration/password_reset_success.html', {})
    
