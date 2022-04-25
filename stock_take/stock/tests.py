from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import *
from .models import Stock, Product, Parts
from .forms import StockForm, PartsForm, ProductForm


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

        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_home_view(self):
        """Test home view"""
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_admin_view_view(self):
        """Test admin view"""
        response = self.client.get(self.admin_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_view.html')

    def test_products_view(self):
        """Test products view"""
        response = self.client.get(self.products_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    def test_add_new_product_view_get(self):
        """Test add new product GET view"""
        response = self.client.get(self.add_new_product_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_product.html')
    
    def test_add_new_stock_part_view_get(self):
        """Test add new stock part GET view"""
        response = self.client.get(self.add_new_stock_part_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_stock_part.html')


class TestForms(TestCase):
    """Test forms"""
    def setUp(self):
        """Setup"""
        self.user = User.objects.create_user(username='testuser', password='12345')
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
