from django import forms
from apps.contacts.models import Contacts
from django.core.validators import RegexValidator
from datetime import datetime

"""
#### STARTING CONTACT FORMS ####
"""


class ContactModelForm(forms.ModelForm):
    name = forms.CharField(
        label='Name and Surname',
        min_length=3,
        max_length=25,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message=" Only letters is allowed!")],
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'First name',
            'class': 'form-control',
        }))
    
    email = forms.CharField(
        label='E-mail',
        min_length=8,
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
                                   message=" Please add to valid E-mail address! ")],
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'E-mail',
            'class': 'form-control',
        }))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(
        attrs={
            'placeholder': 'Subject',
            'class': 'form-control',
        }))

    message = forms.CharField(
        label='Message',
        min_length=4,
        max_length=80,
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Message',
            'class': 'form-control',
        }))

    class Meta:
        model = Contacts
        fields = [
            'name',
            'email',
            'subject',
            'message',
            
        ]