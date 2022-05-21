"""
Imports
"""
from django.test import TestCase
from django.contrib.auth.models import User
from stock.models import Stock, Product
from stock.forms import StockForm, PartsForm, ProductForm


class TestForms(TestCase):
    """Test forms"""
    def setUp(self):
        """Setup"""
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
            )
        login = self.client.login(username='testuser', password='12345')

        self.stock1 = Stock.objects.create(
            name='stock1',
            code='12345',
            number_in_stock=100,
            company=self.user
        )

        self.product1 = Product.objects.create(
            name='product1',
            company=self.user
        )

    def test_stock_form_valid(self):
        """Test valid stock form"""
        form = StockForm(data={
            'name': 'stock1',
            'code': '12345',
            'number_in_stock': 100,
            'company': self.user
        })

        self.assertTrue(form.is_valid())

    def test_stock_form_invalid(self):
        """Test invalid stock form"""
        form = StockForm(data={
            'name': '',
            'code': '12345',
            'number_in_stock': 100,
            'company': self.user
        })

        self.assertFalse(form.is_valid())

    def test_product_form_valid(self):
        """Test valid product form"""
        form = ProductForm(data={
            'name': 'product1',
            'company': self.user
        })

        self.assertTrue(form.is_valid())

    def test_product_form_invalid(self):
        """Test invalid product form"""
        form = ProductForm(data={
            'name': '',
            'company': self.user
        })

        self.assertFalse(form.is_valid())

    def test_parts_form_valid(self):
        """Test valid parts form"""
        form = PartsForm(data={
            'product_part_belongs_to': self.product1,
            'item': self.stock1,
            'number_required': 1,
            'company': self.user
        })

        self.assertTrue(form.is_valid())

    def test_parts_form_invalid(self):
        """Test invalid parts form"""
        form = PartsForm(data={
            'product_part_belongs_to': '',
            'item': self.stock1,
            'number_required': 1,
            'company': self.user
        })

        self.assertFalse(form.is_valid())
