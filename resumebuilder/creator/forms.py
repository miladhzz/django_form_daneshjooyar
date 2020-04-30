from django import forms
from . import models


class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = '__all__'


class ResumeEducationForm(forms.ModelForm):
    class Meta:
        model = models.ResumeEducation
        exclude = ('resume', )


class ResumeSkillForm(forms.ModelForm):
    class Meta:
        model = models.ResumeSkill
        fields = ('skill', 'level', )


class ResumeExperienceForm(forms.ModelForm):
    class Meta:
        model = models.ResumeExperience
        fields = ('company', 'start_date', 'end_date', 'working_now', )
