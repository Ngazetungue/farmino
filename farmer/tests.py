
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


def test_home_page_status_code(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)