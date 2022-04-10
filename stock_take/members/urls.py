"""
Imports
"""
from django.urls import path
from .views import login, password_reset_success
from .views import UserRegisterView, UserEditView, ChangePasswordView

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', ChangePasswordView.as_view(), name="password"),
    path(
        'password_reset/done',
        password_reset_success,
        name='password_reset_success'
        )
]
