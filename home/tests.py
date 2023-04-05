from django.test import TestCase, SimpleTestCase

# Create your tests here.
class simpleTest(SimpleTestCase):
    def test_home_page_status(self):
        reponse = self.client.get('/')
        self.assertEqual(reponse.status_code, 200)
