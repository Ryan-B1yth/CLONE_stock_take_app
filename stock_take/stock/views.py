from django.shortcuts import render
from django.views.generic import ListView
# from .models import Product, Stock
from .forms import ProductForm, StockForm


def create_new_product(request):
    """
    Add a product
    """
    # Create instance of Product model form
    product_form = ProductForm(request.POST)
    if request.method == 'POST':
        product_form.save()
    context = {
        'product_form': product_form,
    }

    return render(request, 'add_product.html', context)


def create_new_stock_part(request):
    """
    Add a stock part
    """
    # Create instance of Stock model form
    stock_form = StockForm(request.POST)
    if request.method == 'POST':
        stock_form.save()
    context = {
        'stock_form': stock_form,
    }

    return render(request, 'add_stock_part.html', context)

    
    
    # # Create instance of Parts model form
    # parts_form = PartsForm(request.POST)
    # if request.method == 'POST':
    #     # Validate
    #     if product_form.is_valid() and parts_form.is_valid():
    #         product_form.save(commit=False)
    #         parts_form.save(commit=False)
    #     else: 
    #         # print(product_form.errors)
    #         print(parts_form.errors)
    # items = Parts.objects.all()
    # context = {
    #     'product_form': product_form,
    #     'parts_form': parts_form,
    #     'items': items
    # }
    return render(request, 'index.html', context)
