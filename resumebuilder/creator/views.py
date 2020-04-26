from django.shortcuts import render
from . import forms


def create_resume(request):
    form = forms.ResumeForm()
    if request.method == 'POST':
        form = forms.ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'create_resume.html', {'form': form})


def create_resume_education(request):
    form = forms.ResumeEducationForm()

    return render(request, 'create_resume_education.html', {'form': form})


def create_resume_skill(request):
    form = forms.ResumeSkillForm()

    return render(request, 'create_resume_skill.html', {'form': form})


def create_resume_experience(request):
    form = forms.ResumeExperienceForm()

    return render(request, 'create_resume_experience.html', {'form': form})
