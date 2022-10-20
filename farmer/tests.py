
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class SimpleTests(SimpleTestCase):
    
    def test_home_page_status_code(self):
        response = self.client.get("home/")
        self.assertEqual(response.status_code, 200)