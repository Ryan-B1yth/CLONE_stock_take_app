from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Parts, Stock


class index(ListView):
    """
    Home page
    """
    model = Product
    template_name = 'index.html'

