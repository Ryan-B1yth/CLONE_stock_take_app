"""
Imports
"""
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Stock(models.Model):
    """
    Stock model
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    number_in_stock = models.IntegerField()
    company = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.name} | {self.code} | {self.number_in_stock}'

    def get_absolute_url(self):
        """
        Required url GET
        """
        return reverse('home')


class Product(models.Model):
    """
    Product model
    """
    name = models.CharField(max_length=100)
    stock_parts = models.ManyToManyField(Stock)
    company = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.name}'


class Parts(models.Model):
    """
    Parts model
    """
    product_part_belongs_to = models.ForeignKey(
        Product, on_delete=models.CASCADE
        )
    item = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE
        )
    number_required = models.IntegerField()
    company = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.company} | {self.product_part_belongs_to} | ' \
            f'{self.item.name} | {self.number_required}'
