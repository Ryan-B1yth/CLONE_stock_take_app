from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Parts, Stock
from .forms import ProductForm, PartsForm


def create_new_product(request):
    """
    Add a product
    """
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        parts_form = PartsForm(request.POST)
        if product_form.is_valid() and parts_form.is_valid():
            product_form.save(commit=False)
            parts_form.save(commit=False)
    product_form = ProductForm()
    parts_form = PartsForm()
    context = {
        'product_form': product_form,
        'parts_form': parts_form,
    }
    return render(request, 'index.html', context)

