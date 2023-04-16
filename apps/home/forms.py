from django import forms
from .models import Project, ProjectTypeChoise,StatusChoise



class ProjectModelForm(forms.ModelForm):
    project_name = forms.CharField(
        label='Project name',
        min_length=3,
        max_length=25,
        
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Project name',
            'class': 'form-control',
        }))
    project_type = forms.ChoiceField(choices=ProjectTypeChoise.choices, required=False, widget=forms.Select(
        attrs={

            'class': 'form-control',

        }))
    company_name = forms.CharField(label='Company Name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Company Name',
            'class': 'form-control',
            'type': 'text',
        }))
    hardware = forms.CharField(label='hardware', widget=forms.TextInput(
        attrs={
            'placeholder': 'hardware',
            'class': 'form-control',
            'type': 'text',
        }))
    software = forms.CharField(label='Software', widget=forms.TextInput(
        attrs={
            'placeholder': 'Software',
            'class': 'form-control',
            'type': 'text',
        }))
    project_start = forms.DateField(label='Project Start Date', widget=forms.TextInput(
        attrs={
            'placeholder': 'Project Start Date',
            'class': 'form-control',
            'type': 'Date'

        }))
    project_finished = forms.DateField(label='Project Finished Date', widget=forms.TextInput(
        attrs={
            'placeholder': 'Project Finished Date',
            'class': 'form-control',
            'type': 'Date'

        }))
    project_location = forms.CharField(label='Project Location', widget=forms.TextInput(
        attrs={
            'placeholder': 'Project Location',
            'class': 'form-control',
            'type': 'text',
        }))
    project_status = forms.ChoiceField(choices=StatusChoise.choices, required=False, widget=forms.Select(
        attrs={

            'class': 'form-control',

        }))
    
    
    class Meta:
        model = Project
        fields = '__all__'

    def clean_first_name(self):
        data = self.cleaned_data["project_name"]
        return data

    def clean(self):
        pass

   
