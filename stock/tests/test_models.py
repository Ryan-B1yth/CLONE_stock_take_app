"""
Imports
"""
from django.test import TestCase
from django.contrib.auth.models import User
from stock.models import Stock, Product, Parts


class TestModels(TestCase):
    """Test all models"""
    def setUp(self):
        self.user = User.objects.create(
            username='test_user',
            password='12345'
            )
        login = self.client.login(username='testuser', password='12345')

        self.test_stock = Stock.objects.create(
            name='test_stock',
            code='0000',
            number_in_stock=1,
            company=self.user
        )

        self.test_product = Product.objects.create(
            name='test_product',
            company=self.user
        )

        self.test_part = Parts.objects.create(
            product_part_belongs_to=self.test_product,
            item=self.test_stock,
            number_required=1,
            company=self.user
        )

    def test_stock_return_string(self):
        """Test stock return string"""
        self.assertEqual(str(self.test_stock), 'test_stock | 0000 | 1')

    def test_product_return_string(self):
        """Test product return string"""
        self.assertEqual(str(self.test_product), 'test_product')

    def test_parts_return_string(self):
        """Test parts return string"""
        self.assertEqual(str(self.test_part), 'test_product test_stock 1')

    def test_get_absolute_url(self):
        """Test get_absolute_url"""
        self.assertEqual('/', Stock.get_absolute_url(self))
