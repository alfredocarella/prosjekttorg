from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, InfoPageView


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_returns_correct_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_uses_home_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Hjemmeside")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This text should NOT be on the page")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class InfoPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("info")
        self.response = self.client.get(url)

    def test_infopage_returns_correct_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_infopage_uses_info_template(self):
        self.assertTemplateUsed(self.response, "info.html")

    def test_infopage_contains_correct_html(self):
        self.assertContains(self.response, "Info")

    def test_infopage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This text should NOT be on the page")

    def test_infopage_url_resolves_infopageview(self):
        view = resolve("/info/")
        self.assertEqual(view.func.__name__, InfoPageView.as_view().__name__)
