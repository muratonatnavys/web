from django.urls import path
from .views import (
 
    ServicePageView,
    BmsPageView,
    EmsPageView,
    PavaPageView,
    AlarmPageView,
    CctvPageView,
    PanelPageView,
    LightingPageView,
    AudioPageView,
    AccessPageView
 
)

app_name = "serivces"

urlpatterns = [

    path('service', ServicePageView.as_view(), name='service'),   
    path('bms', BmsPageView.as_view(), name='bms'), 
    path('ems', EmsPageView.as_view(), name='ems'),
    path('fire', AlarmPageView.as_view(), name='fire'),
    path('pava', PavaPageView.as_view(), name='pava'),
    path('cctv', CctvPageView.as_view(), name='cctv'),
    path('panel', PanelPageView.as_view(), name='panel'),
    path('lighting', LightingPageView.as_view(), name='lighting'),
    path('audio', AudioPageView.as_view(), name='audio'),
    path('access', AccessPageView.as_view(), name='access'),

]