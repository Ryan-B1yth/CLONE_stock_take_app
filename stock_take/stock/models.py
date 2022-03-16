from django.db import models


class Stock(models.Model):
    """
    Stock model
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    number_in_stock = models.IntegerField()

    def __str__(self):
        return f'{self.name} | {self.code}'


class Parts(models.Model):
    """
    Parts model
    """
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    number_required = models.IntegerField()

    def __str__(self):
        return f'{self.item} | {self.number_required}'
    

class Product(models.Model):
    """
    Product model
    """
    name = models.CharField(max_length=100)
    parts = models.ManyToManyField(Parts)

    def __str__(self):
        return f'{self.name}'


