"""
Imports
"""
from django.urls import path
from .views import (
    Login,
    UserRegisterView,
    UserEditView,
    ChangePasswordView,
    password_reset_success
)

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/edit/', UserEditView.as_view(), name="edit_profile"),
    path('password/', ChangePasswordView.as_view(), name="password"),
    path(
        'password_reset/done/',
        password_reset_success,
        name='password_reset_success'
        )
]
