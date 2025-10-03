from django.shortcuts import render
from django.views.generic import TemplateView
from apps.slider.models import Slider
from .models import Visit


#صفحه اصلی و اسلایدر و تعداد بازدید سایت
def index(request):
    # visit همیشه داریم
    visit, created = Visit.objects.get_or_create(id=1)

    # فقط اگه کاربر قبلاً بازدید نکرده باشه
    if not request.session.get('has_visited'):
        visit.count += 1
        visit.save()
        request.session['has_visited'] = True

    sliders = Slider.objects.filter(is_active=True).order_by('create_at')

    return render(request, "main/index.html", {"sliders": sliders, "visit": visit.count})




    

class ContactView(TemplateView):
    template_name = 'footer/contact.html'
    
    
class AboutView(TemplateView):
    template_name = 'footer/about.html'
    

class ResumeView(TemplateView):
    template_name = 'header/resume.html'

class ProjectsView(TemplateView):
    template_name = 'header/projects.html'





