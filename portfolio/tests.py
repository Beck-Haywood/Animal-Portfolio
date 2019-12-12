from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class PortfolioRouteTests(TestCase):

    def test_homepage(self):
        """
        Tests homepage        
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_uploadpage(self):
        """
        Tests homepage        
        """
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 301)

    
