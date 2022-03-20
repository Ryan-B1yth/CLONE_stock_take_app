from django.contrib import admin
from django.urls import path
from .views import (
    create_new_product,
    create_new_stock_part,
    add_parts_to_product,
    home,
    product_detail
    )

urlpatterns = [
    path('', home, name='home'),
    path('add-product/', create_new_product, name='add_new_product'),
    path('add-stock/', create_new_stock_part, name='add_new_stock_part'),
    path('link/', add_parts_to_product, name='add_parts_to_product'),
    path('product-detail/<int:pk>', product_detail, name='product-detail')
]
