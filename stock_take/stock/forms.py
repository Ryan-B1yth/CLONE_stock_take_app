from django import forms
from .models import Product, Parts


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


class PartsForm(forms.ModelForm):
    """
    Add parts to product
    """
    class Meta:
        """
        Meta data
        """
        model = Parts
        fields = ['item', 'number_required']

        
