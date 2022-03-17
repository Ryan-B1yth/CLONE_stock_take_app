from django.contrib import admin
from django.urls import path
from .views import create_new_product

urlpatterns = [
    path('', create_new_product, name='index'),
]
