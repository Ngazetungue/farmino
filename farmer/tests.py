from django.urls import reverse

from django.test import TestCase


def test_home_page_status_code(self):
    response = self.client.get("/home/")
    self.assertEquals(response.status_code, 200)


def test_farmer_list_view(self):
    response = self.client.get(reverse("farmer-list"))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Ziddan")
    self.assertTemplateUsed(response, "farmer/pages/tables.html")
