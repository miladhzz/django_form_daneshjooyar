from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

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
        widgets ={
            'working_now': forms.NullBooleanSelect
        }


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )
