from django.views.generic import ListView
from .models import Skill


class SkillListView(ListView):
    model = Skill
    template_name = 'skills/skills.html'
    context_object_name = 'skills'
