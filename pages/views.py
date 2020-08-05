# from django.shortcuts import render
from django.views.generic import TemplateView


class InfoPageView(TemplateView):
    template_name = "info.html"
