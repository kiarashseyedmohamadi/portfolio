from django.urls import path
from .views import IndexView,ContactView,AboutView,ProjectsView,SkillsView,ResumeView,BlogView

app_name = 'main'  
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('about/',AboutView.as_view(), name='about'),
    path('projects/',ProjectsView.as_view(), name='projects'),
    path('skills/',SkillsView.as_view(), name='skills'),
    path('resume/',ResumeView.as_view(), name='resume'),
    path('blog/',BlogView.as_view(), name='blog'),
]
