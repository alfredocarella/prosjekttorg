from django.test import Client, TestCase
from django.urls import reverse

from .models import Project


class ProjectTests(TestCase):
    def setUp(self):
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

    def test_project_list_view(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A moonshot')
        self.assertTemplateUsed(response, 'projects/project_list.html')

    def test_project_detail_view(self):
        response = self.client.get(self.project.get_absolute_url())
        no_response = self.client.get('/projects/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A moonshot')
        self.assertTemplateUsed(response, 'projects/project_detail.html')
