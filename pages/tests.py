from django.test import SimpleTestCase
from django.urls import reverse

"""
Generally speaking,
- SimpleTestCase is used when a database is unnecessary
- TestCase is used when you want to test the database
- TransactionTestCase is helpful to directly test database transactions
- LiveServerTestCase launches a live server thread for testing with browser-based tools like Selenium.
"""


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  # new
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("pages:home"))
        self.assertTemplateUsed(response, "pages/home.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  # new
        response = self.client.get(reverse("pages:about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("pages:about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "<h1>About page</h1>")
