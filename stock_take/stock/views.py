"""
Imports
"""
import math
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Stock, Parts
from .forms import ProductForm, StockForm, PartsForm


def home(request):
    """
    Home page
    """
    return render(request, 'home.html', {})


def product_page(request):
    """
    Product page
    """
    default_user = request.user
    products = Product.objects.filter(company=default_user)
    number_to_be_made = {}

    for product in products:
        # Get the parts for the products
        parts = Parts.objects.filter(
            product_part_belongs_to=product.id
            )
        units = {}
        amount = []
        total_units_to_be_made = {}
        for i in parts:
            # Divide the number of each part in stock by
            # the number of each part required
            units_to_make = (i.item.number_in_stock / i.number_required)
            units_to_make = math.floor(units_to_make)
            units[i.product_part_belongs_to] = units_to_make
            amount.append(units_to_make)
        # Returns multiple amounts for each product
        # Sort and return the first (smallest)
        amount.sort()
        amount = amount[:1]
        # Set empty lists to 0
        if len(amount) == 0 or amount[0] == 0:
            total_units_to_be_made = 0
        else:
            # Integer the others
            for num in amount:
                int(num)
                total_units_to_be_made = num
        # Add key, value pairs to the dict
        number_to_be_made[product.id] = total_units_to_be_made

    context = {
        'products': products,
        'number_to_be_made': number_to_be_made,
        'default_user': default_user
    }
    return render(request, 'products.html', context)


def stock_page(request):
    """
    Stock page
    """
    default_user = request.user
    stock = Stock.objects.filter(company=default_user)
    context = {
        'stock': stock,
    }
    return render(request, 'stock.html', context)


def create_new_product(request):
    """
    Add a product
    """
    default_user = request.user
    # Create instance of Product model form
    product_form = ProductForm(
        request.POST or None,
        initial={
            'company': default_user
            }
        )
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect('link/')
    context = {
        'product_form': product_form,
    }

    return render(request, 'add_product.html', context)


def create_new_stock_part(request):
    """
    Add a stock part
    """
    default_user = request.user
    # Create instance of Stock model form
    stock_form = StockForm(
        request.POST or None,
        initial={
            'company': default_user
            }
        )
    if request.method == 'POST':
        if stock_form.is_valid():
            stock_form.save()
            return HttpResponseRedirect('/stock/')

    context = {
        'stock_form': stock_form,
    }

    return render(request, 'add_stock_part.html', context)


def add_parts_to_product(request):
    """
    Add parts to a product
    """
    default_user = request.user
    default_product = Product.objects.filter(company=default_user).latest('id')
    parts_form = PartsForm(
        request.POST or None,
        initial={
            'product_part_belongs_to': default_product,
            'company': default_user
            },
        )
    parts_form.fields["item"].queryset = Stock.objects.filter(company=default_user)
    added_part = []
    context = {}
    if request.method == 'POST':
        if parts_form.is_valid():
            parts_form.save()
        if len(added_part) == 0:
            added = Parts.objects.latest('id')
            added_part.append(added.item.name)
            added_part = added_part[0]
            context['added_part'] = added_part

    context['default_product'] = default_product
    context['parts_form'] = parts_form
    context['default_user'] = default_user

    return render(request, 'link_parts_to_product.html', context)


def add_more_parts(request, pk):
    """
    Add parts to a product
    """
    default_user = request.user
    default_product = Product.objects.filter(company=default_user).filter(id=pk).latest('id')
    parts_form = PartsForm(
        request.POST or None,
        initial={
            'product_part_belongs_to': default_product,
            'company': default_user,
            },
        )
    parts_form.fields["item"].queryset = Stock.objects.filter(company=default_user)
    added_part = []
    context = {}
    if request.method == 'POST':
        if parts_form.is_valid():
            parts_form.save()
        if len(added_part) == 0:
            added = Parts.objects.latest('id')
            added_part.append(added.item.name)
            added_part = added_part[0]
            context['added_part'] = added_part

    context['default_product'] = default_product
    context['parts_form'] = parts_form
    context['default_user'] = default_user

    return render(request, 'add_more_parts.html', context)


def product_detail(request, pk):
    """
    Show all parts to product
    """
    default_user = request.user
    product_parts = Parts.objects.filter(company=default_user).filter(product_part_belongs_to=pk)
    product = Product.objects.filter(company=default_user).filter(id=pk).first()
    context = {
        'product_parts': product_parts,
        'product': product,
    }
    return render(request, 'product_detail.html', context)


class UpdateStock(UpdateView):
    """
    Update stock
    """
    model = Stock
    template_name = 'update_stock.html'
    form_class = StockForm
    success_url = reverse_lazy('stock')


class DeleteStockView(DeleteView):
    """
    Delete an item from stock model
    """
    model = Stock
    template_name = 'delete_stock.html'
    success_url = reverse_lazy('stock')


class DeletePartView(DeleteView):
    """
    Delete a part from part model
    """
    model = Parts
    template_name = 'delete_part.html'
    success_url = reverse_lazy('products')


class DeleteProductView(DeleteView):
    """
    Delete aproduct from product model
    """
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('home')
