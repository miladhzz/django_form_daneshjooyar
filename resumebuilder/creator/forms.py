from django import forms
from . import models


class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = '__all__'


class ResumeEducationForm(forms.ModelForm):
    class Meta:
        model = models.ResumeEducation
        fields = '__all__'


class ResumeSkillForm(forms.ModelForm):
    class Meta:
        model = models.ResumeSkill
        fields = '__all__'


class ResumeExperienceForm(forms.ModelForm):
    class Meta:
        model = models.ResumeExperience
        fields = '__all__'
