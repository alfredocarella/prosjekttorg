from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView


urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<uuid:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('<uuid:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('<uuid:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),
]
