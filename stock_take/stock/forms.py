from django import forms
from .models import Product, Stock, Parts


class ProductForm(forms.ModelForm):
    """
        Add a product form
    """
    class Meta:
        """
            Add product form meta data
        """
        model = Product
        fields = ['name']


class StockForm(forms.ModelForm):
    """
    Add a part
    """
    class Meta:
        """
        Meta data
        """
        model = Stock
        fields = '__all__'


class PartsForm(forms.ModelForm):
    """
    Add parts to product
    """
    class Meta:
        """
        Meta data
        """
        model = Parts
        fields = '__all__'

        widgets = {
            # 'product_part_belongs_to': forms.HiddenInput()
        }
