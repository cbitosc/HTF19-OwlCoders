from django import forms
from django.db import models
from .models import SkillSet

class AddSkill(forms.ModelForm):
    class Meta:
        model = SkillSet
        fields = (
            'languages',
            'frameworks',
            'gpa',
            'company',
        )
