from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Course, Project


class HomeView(ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet for all published projects
        context['project_list'] = Project.objects.filter(published=True)
        return context


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projects/dashboard.html'
    login_url = 'account_login'


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'
    login_url = 'account_login'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'image', 'courses']
    template_name = 'projects/project_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['title', 'description', 'image', 'courses']
    template_name = 'projects/project_update.html'

    def get_object(self):
        project = super(ProjectUpdateView, self).get_object()
        if not project.user == self.request.user:
            raise Http404
        return project


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        project = super(ProjectDeleteView, self).get_object()
        if not project.user == self.request.user:
            raise Http404
        return project
