"""
Imports
"""
from django.test import TestCase
from django.urls import reverse, resolve
from stock.views import (
    home,
    admin_view,
    product_page,
    create_new_product,
    create_new_stock_part,
    add_parts_to_product,
    product_detail
)


class TestUrls(TestCase):
    """
    Test url resolve
    """
    def test_home_url_is_resolved(self):
        """Test home"""
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_admin_view_url_is_resolved(self):
        """Test admin view"""
        url = reverse('admin_view')
        self.assertEqual(resolve(url).func, admin_view)

    def test_products_url_is_resolved(self):
        """Test products"""
        url = reverse('products')
        self.assertEqual(resolve(url).func, product_page)

    def test_add_product_url_is_resolved(self):
        """Test add product"""
        url = reverse('add_new_product')
        self.assertEqual(resolve(url).func, create_new_product)

    def test_add_stock_url_is_resolved(self):
        """Test add stock"""
        url = reverse('add_new_stock_part')
        self.assertEqual(resolve(url).func, create_new_stock_part)

    def test_link_url_is_resolved(self):
        """Test link"""
        url = reverse('add_parts_to_product')
        self.assertEqual(resolve(url).func, add_parts_to_product)

    def test_product_detail_url_is_resolved(self):
        """Test product detail"""
        url = reverse('product-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, product_detail)
