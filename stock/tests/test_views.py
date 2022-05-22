"""
Imports
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from stock.models import Stock, Product, Parts


class TestViews(TestCase):
    """Test views"""
    def setUp(self):
        """Set up """
        self.client = Client()
        self.home_url = reverse('home')
        self.admin_view_url = reverse('admin_view')
        self.products_url = reverse('products')
        self.stock_url = reverse('stock')
        self.add_new_product_url = reverse('add_new_product')
        self.add_new_stock_part_url = reverse('add_new_stock_part')
        self.add_parts_to_product_url = reverse('add_parts_to_product')
        self.add_more_parts_url = reverse('add_more_parts', kwargs={'pk': 1})
        self.product_detail_url = reverse('product-detail', kwargs={'pk': 1})

        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
            )
        login = self.client.login(username='testuser', password='12345')

        self.test_stock = Stock.objects.create(
            name='test_stock',
            code='0000',
            number_in_stock=100,
            company=self.user
        )

        self.test_product = Product.objects.create(
            name='test_product',
            company=self.user
        )

        self.test_part = Parts.objects.create(
            product_part_belongs_to=self.test_product,
            item=self.test_stock,
            number_required=5,
            company=self.user
        )

    def test_home_view(self):
        """Test home view"""
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/home.html')

    def test_admin_view_view(self):
        """Test admin view"""
        response = self.client.get(self.admin_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/admin_view.html')

    def test_products_view(self):
        """Test products view"""
        response = self.client.get(self.products_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/products.html')

    def test_stock_view(self):
        """Test stock view"""
        response = self.client.get(self.stock_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/stock.html')

    def test_add_new_product_view_get(self):
        """Test add new product GET view"""
        response = self.client.get(self.add_new_product_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/add_product.html')

    def test_add_new_stock_part_view_get(self):
        """Test add new stock part GET view"""
        response = self.client.get(self.add_new_stock_part_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/add_stock_part.html')
    
    def test_add_parts_to_product_view_get(self):
        """Test add parts to product GET view"""
        response = self.client.get(self.add_parts_to_product_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/link_parts_to_product.html')

    def test_add_more_parts_get(self):
        """Test add more parts GET view"""
        response = self.client.get(self.add_more_parts_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/add_more_parts.html')

    def test_product_detail_view(self):
        """Test product detail view"""
        response = self.client.get(self.product_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/product_detail.html')
