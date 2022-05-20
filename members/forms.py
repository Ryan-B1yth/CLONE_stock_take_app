"""
Imports
"""
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    """
    Login
    """
    username = forms.CharField()
    password = forms.CharField()


class SignUpForm(UserCreationForm):
    """
    Sign up form
    """
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First name'
                }
                ))
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name'
                }
                ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
                }
                ))
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Create a password'
                }
                ))
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Verify password'
                }
                ))

    class Meta:
        """
        Sign up form meta data
        """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )


class EditProfileForm(UserChangeForm):
    """
    Update user info
    """
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'First name'
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Last name'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email'
    }))

    class Meta:
        """
        User edit Meta data
        """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            )


class ChangePasswordForm(PasswordChangeForm):
    """
    Update password
    """
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Old password'
        }))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'New password'
        }))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Verify password'
        }))

    class Meta:
        """
        User edit Meta data
        """
        model = User
        fields = (
            'old_password',
            'new_password1',
            'new_password2',
        )
