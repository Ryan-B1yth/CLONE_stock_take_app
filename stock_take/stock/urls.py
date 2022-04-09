from django.contrib import admin
from django.urls import path
from .views import (
    create_new_product,
    # CreateNewProduct,
    create_new_stock_part,
    add_parts_to_product,
    home,
    stock_page,
    product_page,
    product_detail,
    UpdateStock,
    DeletePartView,
    DeleteProductView,
    DeleteStockView,
    add_more_parts
    )

urlpatterns = [
    path('', home, name='home'),
    path('stock/', stock_page, name='stock'),
    path('products/', product_page, name='products'),
    path('add-product/', create_new_product, name='add_new_product'),
    # path('add-product/', CreateNewProduct.as_view(), name='add_new_product'),
    path('add-stock/', create_new_stock_part, name='add_new_stock_part'),
    path('add-product/link/', add_parts_to_product, name='add_parts_to_product'),
    path('add-product/link/<int:pk>', add_more_parts, name='add_more_parts'),
    path('product-detail/<int:pk>', product_detail, name='product-detail'),
    path('adjust-stock/<int:pk>', UpdateStock.as_view(), name='update-stock'),
    path(
        'delete-part/<int:pk>',
        DeletePartView.as_view(),
        name='delete-part'
        ),
    path(
        'delete-stock/<int:pk>',
        DeleteStockView.as_view(),
        name='delete-stock'
        ),
    path(
        'delete-product/<int:pk>',
        DeleteProductView.as_view(),
        name='delete-product'
        ),
]
