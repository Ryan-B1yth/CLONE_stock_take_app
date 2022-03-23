from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Product, Stock, Parts
from .forms import ProductForm, StockForm, PartsForm


def home(request):
    """
    Home page
    """
    products = Product.objects.all()
    stock = Stock.objects.all()
    context = {
        'products': products,
        'stock': stock,
    }
    return render(request, 'home.html', context)


def product_page(request):
    """
    Home page
    """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products.html', context)


def stock_page(request):
    """
    Stock page
    """
    stock = Stock.objects.all()
    context = {
        'stock': stock,
    }
    return render(request, 'stock.html', context)


# def create_new_product(request):
#     """
#     Add a product
#     """
#     # Create instance of Product model form
#     product_form = ProductForm(request.POST)
#     if request.method == 'POST':
#         if product_form.is_valid():
#             product_form.save()
#     context = {
#         'product_form': product_form,
#     }

#     return render(request, 'add_product.html', context)


class CreateNewProduct(CreateView):
    """
    Add a product
    """
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = 'link/'


def create_new_stock_part(request):
    """
    Add a stock part
    """
    # Create instance of Stock model form
    stock_form = StockForm(request.POST)
    if request.method == 'POST':
        if stock_form.is_valid():
            stock_form.save()
    context = {
        'stock_form': stock_form,
    }

    return render(request, 'add_stock_part.html', context)


def add_parts_to_product(request):
    """
    Add parts to a product
    """
    default_product = Product.objects.latest('id')
    parts_form = PartsForm(
        request.POST or None,
        initial={'product_part_belongs_to': default_product},
        )
    if request.method == 'POST':
        if parts_form.is_valid():
            parts_form.save()
    context = {
        # 'default_product': default_product,
        'parts_form': parts_form,
    }

    return render(request, 'link_parts_to_product.html', context)


def product_detail(request, pk):
    """
    Show all parts to product
    """
    product_parts = Parts.objects.filter(product_part_belongs_to=pk)
    product = Product.objects.filter(id=pk).first()
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


class DeleteStockView(DeleteView):
    """
    Delete an item from stock model
    """
    model = Stock
    template_name = 'delete_stock.html'
    success_url = reverse_lazy('home')


class DeletePartView(DeleteView):
    """
    Delete a part from part model
    """
    model = Parts
    template_name = 'delete_part.html'
    success_url = reverse_lazy('home')


class DeleteProductView(DeleteView):
    """
    Delete aproduct from product model
    """
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('home')




# def update_stock(request):
#     """
#     Update stock
#     """
#     stock_form = StockForm(request.POST)
#     if request.method == 'POST':
#         if stock_form.is_valid():
#             stock_form.save()
#     context = {
#         'stock_form': stock_form,
#     }
#     return render(request, 'update_stock.html', context)


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
    
