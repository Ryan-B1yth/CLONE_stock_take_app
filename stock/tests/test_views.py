"""
Imports
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    """Test views"""
    def setUp(self):
        """Set up """
        self.client = Client()
        self.home_url = reverse('home')
        self.admin_view_url = reverse('admin_view')
        self.products_url = reverse('products')
        self.add_new_product_url = reverse('add_new_product')
        self.add_new_stock_part_url = reverse('add_new_stock_part')
        self.add_parts_to_product_url = reverse('add_parts_to_product')
        self.product_detail_url = reverse('product-detail', kwargs={'pk': 1})

        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
            )
        login = self.client.login(username='testuser', password='12345')

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
