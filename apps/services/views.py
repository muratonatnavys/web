from django.views.generic.base import TemplateView
from django.shortcuts import reverse
from django.views import generic

class ServicePageView(TemplateView):

    template_name = "service/service.html" # templates/service.html


class BmsPageView(TemplateView):

    template_name = "service/bms.html" # templates/bms.html

class EmsPageView(TemplateView):

    template_name = "service/ems.html" # templates/ems.html

class AlarmPageView(TemplateView):

    template_name = "service/alarm.html" # templates/alarm.html


class PavaPageView(TemplateView):

    template_name = "service/pava.html" # templates/pava.html

class CctvPageView(TemplateView):

    template_name = "service/cctv.html" # templates/cctv.html

class PanelPageView(TemplateView):

    template_name = "service/panel.html" # templates/panel.html

class LightingPageView(TemplateView):

    template_name = "service/lighting.html" # templates/lighting.html

class AudioPageView(TemplateView):

    template_name = "service/audio.html" # templates/audio.html

class AccessPageView(TemplateView):

    template_name = "service/access.html" # templates/access.html