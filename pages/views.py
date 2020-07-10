# from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class InfoPageView(TemplateView):
    template_name = "info.html"
