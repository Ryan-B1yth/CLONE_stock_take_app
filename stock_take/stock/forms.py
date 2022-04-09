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
        fields = ['name', 'company']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Product Name'
                }
            )
        }


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

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Stock Item Name'
                }
            ),
            'code': forms.TextInput(
                attrs={
                    'placeholder': 'Stock Item Code'
                }
            ),
            'number_in_stock': forms.TextInput(
                attrs={
                    'placeholder': 'Number in Stock'
                }
            )
        }


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
            'product_part_belongs_to': forms.HiddenInput(),
            'number_required': forms.TextInput(
                attrs={
                    'placeholder': 'Number Required'
                }
            )
        }
