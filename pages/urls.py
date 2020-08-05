from django.urls import path
from .views import InfoPageView


urlpatterns = [
    path("info/", InfoPageView.as_view(), name="info"),
]
