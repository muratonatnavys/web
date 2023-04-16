from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.db import models
from datetime import date
from django.utils import timezone
from django.utils.html import format_html


class ProjectTypeChoise(models.TextChoices):
    bms_project = 'BMS Project', _('BMS Project')
    elv_project = 'ELV Project', _('ELV Project')
    lighting_fixture = 'Lighting Fixture', _('Lighting Fixture')
    audio_video = 'Design Project', _('Design Project')
    


class StatusChoise(models.TextChoices):
    active = 'Active', _('Active')
    passive = 'Passive', _('Passive')


class Project(models.Model):

    project_name = models.CharField(max_length=50)
    project_type = models.CharField(
        max_length=35,
        choices=ProjectTypeChoise.choices,
        default=ProjectTypeChoise.bms_project,
        verbose_name='Project Type')
    company_name = models.CharField(max_length=200)
    project_start = models.DateField()
    project_finished = models.DateField()
    project_location = models.CharField(max_length=100)
    project_status = models.CharField(
        max_length=35,
        choices=StatusChoise.choices,
        default=StatusChoise.active,
        verbose_name='Status')
    project_image = models.ImageField(null=True, blank=True,upload_to="images/")

    def __str__(self):
        return self.project_name
    

class ProjectSotware(models.Model):

    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, null= True,)
    software = models.CharField(max_length=200)

    def __str__(self):
        return str(self.project_name)
    
    
class ProjectHardware(models.Model):

    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, null= True,)
    hardware = models.CharField(max_length=200)

    def __str__(self):
        return str(self.project_name)

