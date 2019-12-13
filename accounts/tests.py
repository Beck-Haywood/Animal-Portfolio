from django.test import TestCase

# Create your tests here.
class AccountsRouteTests(TestCase):

    def test_login(self):
        """
        Tests login        
        """
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
    def test_signup(self):
        """
        Tests signup        
        """
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)