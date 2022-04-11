"""
Imports
"""
from django.urls import path
# from django.contrib.auth.views import LoginView
from .views import password_reset_success
from .views import Login, UserRegisterView, UserEditView, ChangePasswordView
from .forms import LoginForm

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', ChangePasswordView.as_view(), name="password"),
    path(
        'password_reset/done',
        password_reset_success,
        name='password_reset_success'
        )
]
