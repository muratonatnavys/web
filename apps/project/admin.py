
from django.contrib import admin
from django.utils.html import format_html
from .models import Project,ProjectHardware,ProjectSotware

class ProjectAdmin(admin.ModelAdmin):
    list_filter = ['project_name']
    list_display = ['project_name', 'project_type', 'company_name',  'project_status']
    search_fields = ['project_name', 'project_type', 'company_name', 'project_status']

class ProjectHardwareAdmin(admin.ModelAdmin):
    list_filter = ['project_name']
    list_display = ['project_name', 'hardware', ]
    search_fields = ['project_name', 'hardware', ]

class ProjectSoftwareAdmin(admin.ModelAdmin):
    list_filter = ['project_name']
    list_display = ['project_name', 'software', ]
    search_fields = ['project_name', 'software', ]



admin.site.register(Project, ProjectAdmin),
admin.site.register(ProjectHardware, ProjectHardwareAdmin),
admin.site.register(ProjectSotware, ProjectSoftwareAdmin),

