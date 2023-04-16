from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.shortcuts import reverse
from django.views import generic
from .models import Project,ProjectHardware,ProjectSotware

class ProjectPageView(ListView):
    model=Project

    template_name = "projects/projects.html" # templates/about.html

class ProjectActiveListView( generic.ListView):
    template_name = 'projects/active.html'
    queryset = Project.objects.all().filter(project_status='Active')
    context_object_name = "projects"

class ProjectPassiveListView( generic.ListView):
    template_name = 'projects/passive.html'
    queryset = Project.objects.all().filter(project_status='Passive')
    context_object_name = "projects"

   
class ProjectDetailView(DetailView):
    template_name = 'projects/details.html'
    queryset = Project.objects.all()
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        projects = super(ProjectDetailView, self).get_context_data(**kwargs)
        projects ['hardware']= ProjectHardware.objects.filter(project_name=self.kwargs['pk'])
        projects ['sofware']= ProjectSotware.objects.filter(project_name=self.kwargs['pk'])
        
        return projects