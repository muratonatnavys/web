from django.views.generic.base import TemplateView
from django.shortcuts import reverse
from django.views import generic

class AboutPageView(TemplateView):

    template_name = "about/about.html" # templates/about.html
