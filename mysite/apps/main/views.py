from django.shortcuts import render
from django.views.generic import TemplateView
from apps.slider.models import Slider


def index(request):
    sliders = Slider.objects.filter(is_active=True).order_by('create_at')
    return render(request, "main/index.html", {"sliders": sliders})


    

class ContactView(TemplateView):
    template_name = 'footer/contact.html'
    
    
class AboutView(TemplateView):
    template_name = 'footer/about.html'
    

class ResumeView(TemplateView):
    template_name = 'header/resume.html'

class ProjectsView(TemplateView):
    template_name = 'header/projects.html'


