from django.views.generic.base import TemplateView
from django.shortcuts import reverse
from django.views import generic

class HomePageView(TemplateView):

    template_name = "home.html" # templates/home.html

