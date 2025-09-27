from django.shortcuts import render


from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'main/index.html' 
    

class ContactView(TemplateView):
    template_name = 'footer/contact.html'
    
    
class AboutView(TemplateView):
    template_name = 'footer/about.html'
    

class ResumeView(TemplateView):
    template_name = 'header/resume.html'

class SkillsView(TemplateView):
    template_name = 'header/skills.html'

class ProjectsView(TemplateView):
    template_name = 'header/projects.html'

class BlogView(TemplateView):
    template_name = 'header/blog.html'
