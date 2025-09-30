from django.urls import path
from .views import index,ContactView,AboutView,ProjectsView,ResumeView

app_name = 'main'  
urlpatterns = [
    path('', index, name='index'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('about/',AboutView.as_view(), name='about'),
    path('projects/',ProjectsView.as_view(), name='projects'),
    path('resume/',ResumeView.as_view(), name='resume'),
   
]
