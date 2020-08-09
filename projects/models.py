import uuid
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class Course(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.code} - {self.name}'


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = CloudinaryField('image', blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])
