from django.test import TestCase, SimpleTestCase

# Create your tests here.
class simpleTests(SimpleTestCase):
    def test_home_page_status(self):
        reponse = self.client.get('/')
        self.assertEqual(reponse.status_code, 200)
