from django.urls import path
from .views import (

    
    ProjectPageView,
    ProjectActiveListView,
    ProjectPassiveListView,
    ProjectDetailView,
 
)

app_name = "projects"

urlpatterns = [

   
    path('projects', ProjectPageView.as_view(), name='projects'),   
    path('active', ProjectActiveListView.as_view(), name='active'),  
    path('passive', ProjectPassiveListView.as_view(), name='passive'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail'),
]
