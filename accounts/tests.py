from django.test import TestCase

# Create your tests here.
class AccountsRouteTests(TestCase):

    def test_login(self):
        """
        Tests login        
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def signup(self):
        """
        Tests signup        
        """
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 301)