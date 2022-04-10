"""
Imports
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    """
    Sign up form
    """
    username = forms.TextInput()
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Create a password'
        }
    )
    )
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Verify password'
        }
    )
    )

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

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            )
        }
