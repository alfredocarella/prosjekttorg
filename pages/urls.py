from django.urls import path
from .views import HomePageView, InfoPageView


urlpatterns = [
    path("info/", InfoPageView.as_view(), name="info"),
    path("", HomePageView.as_view(), name="home"),
]
