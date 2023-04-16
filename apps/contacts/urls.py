from django.urls import path
from .views import (

    
    ContactCreateView,
 
)

app_name = "contacts"

urlpatterns = [

   
    path('contacts', ContactCreateView.as_view(), name='contacts'),   

]
