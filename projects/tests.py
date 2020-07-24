from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client, TestCase
from django.urls import reverse

from .models import Project


class ProjectTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='newuser',
            email='newuser@email.com',
            password='testpass123'
        )
        self.project = Project.objects.create(
            title="A moonshot",
            description="The Baltimore Gun Club wants shoot the Moon.",
            owner="Alfredo C.",
        )

    def test_project_entry(self):
        self.assertEqual(f'{self.project.title}', 'A moonshot')
        self.assertEqual(f'{self.project.description}',
        "The Baltimore Gun Club wants shoot the Moon.")
        self.assertEqual(f'{self.project.owner}', 'Alfredo C.')

    def test_project_list_view_for_logged_in_user(self):
        self.client.login(email='newuser@email.com', password='testpass123')
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A moonshot')
        self.assertTemplateUsed(response, 'projects/project_list.html')

    def test_project_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('project_list'))
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
