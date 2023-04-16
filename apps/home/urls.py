from django.contrib import admin
from django.urls import path
from apps.home.views import HomePageView

app_name = "homes"


urlpatterns = [


    path('', HomePageView.as_view(), name='home'),
   
]