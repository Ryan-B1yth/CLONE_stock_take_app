from django.db import models
from django.urls import reverse


class Stock(models.Model):
    """
    Stock model
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    number_in_stock = models.IntegerField()

    def __str__(self):
        return f'{self.name} | {self.code} | {self.number_in_stock}'
    
    def get_absolute_url(self):
        return reverse('home')


class Product(models.Model):
    """
    Product model
    """
    name = models.CharField(max_length=100)
    # parts = models.OneToOneField(Parts, on_delete=models.CASCADE)
    stock_parts = models.ManyToManyField(Stock)

    def __str__(self):
        return f'{self.name}'


class Parts(models.Model):
    """
    Parts model
    """
    product_part_belongs_to = models.ForeignKey(
        Product, on_delete=models.CASCADE
        )
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    number_required = models.IntegerField()

    def __str__(self):
        return f'{self.product_part_belongs_to} {self.item.name} {self.number_required}'
