from django.contrib import admin
from .models import Stock, Product

admin.site.register(Stock)
# admin.site.register(Parts)
admin.site.register(Product)
