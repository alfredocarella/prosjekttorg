from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client, SimpleTestCase, TestCase
from django.urls import resolve, reverse

from .models import Course, Project
from .views import HomeView


class HomepageTests(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url, HTTP_ACCEPT_LANGUAGE='en')

    def test_homepage_returns_correct_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_uses_home_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_english_contains_correct_language(self):
        self.assertContains(self.response, "Assembling")
        self.assertNotContains(self.response, "Dashbord")

    def test_homepage_norwegian_contains_correct_language(self):
        url = reverse("home")
        response = self.client.get(url, HTTP_ACCEPT_LANGUAGE='no')
        self.assertContains(response, "Logg inn")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomeView.as_view().__name__)


class ProjectTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='newuser',
            email='newuser@email.com',
            password='testpass123'
        )
        self.course = Course.objects.create(
            code='MAPE1300',
            name='Mekanikk'
        )
        self.project = Project.objects.create(
            title="A moonshot",
            description="The Baltimore Gun Club wants shoot the Moon.",
            user=self.user,
        )
        self.project.courses.add(self.course)

    def test_project_entry(self):
        self.assertEqual(f'{self.project.title}', 'A moonshot')
        self.assertEqual(f'{self.project.description}',
        "The Baltimore Gun Club wants shoot the Moon.")
        self.assertEqual(f'{self.project.user.email}', 'newuser@email.com')
        courses = self.project.courses.all()
        self.assertEqual(len(courses), 1)
        self.assertEqual(f'{courses[0].code}', 'MAPE1300')
        self.assertEqual(f'{courses[0].name}', 'Mekanikk')

    def test_dashboard_view_for_logged_in_user(self):
        self.client.login(email='newuser@email.com', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A moonshot')
        self.assertTemplateUsed(response, 'projects/dashboard.html')

    def test_dashboard_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{reverse("account_login")}?next=/projects/')
        response = self.client.get(f'{reverse("account_login")}?next=/projects/')
        self.assertContains(response, 'Logg inn')

    def test_project_detail_view_for_logged_in_user(self):
        self.client.login(email='newuser@email.com', password='testpass123')
        response = self.client.get(self.project.get_absolute_url())
        no_response = self.client.get('/projects/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A moonshot')
        self.assertTemplateUsed(response, 'projects/project_detail.html')

    def test_project_detail_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(self.project.get_absolute_url())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{reverse("account_login")}?next={self.project.get_absolute_url()}')
        response = self.client.get(f'{reverse("account_login")}?next={self.project.get_absolute_url()}')
        self.assertContains(response, 'Logg inn')
