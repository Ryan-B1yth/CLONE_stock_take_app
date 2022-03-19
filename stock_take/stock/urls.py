from django.contrib import admin
from django.urls import path
from .views import create_new_product, create_new_stock_part

urlpatterns = [
    path('', create_new_product, name='add_new_product'),
    path('add-stock/', create_new_stock_part, name='add_new_stock_part'),
]
