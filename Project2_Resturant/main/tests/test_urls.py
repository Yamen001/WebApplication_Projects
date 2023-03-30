from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    
    
    def setup(self):
        self.client = Client()
        
    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_contact_view(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        
    def test_handleBlog_view(self):
        url = reverse('handleBlog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        
    def test_chefs_view(self):
        url = reverse('chefs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chefs.html')
        
    def test_order_view(self):
        url = reverse('order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order.html')
        
    def test_error_404_view(self):
        url = reverse('404_error_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404_error.html')