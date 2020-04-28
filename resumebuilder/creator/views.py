from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from . import forms
from . import models
from django.urls import reverse


def create_resume(request):
    form = forms.ResumeForm()
    if request.method == 'POST':
        form = forms.ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            return HttpResponseRedirect(reverse('creator:edit_resume', args=(resume.id, )))
    return render(request, 'create_resume.html', {'form': form})


def edit_resume(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id)
    form = forms.ResumeForm(instance=resume)
    return render(request, 'create_resume.html', {'form': form})


def create_resume_education(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id)
    educations = models.ResumeEducation.objects.filter(resume=resume)
    print(educations)
    form = forms.ResumeEducationForm()
    if request.method == 'POST':
        form = forms.ResumeEducationForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.ResumeEducationForm()

    return render(request, 'create_resume_education.html',
                  {'form': form,
                   'educations': educations,
                   'resume_id': resume.id})


def create_resume_skill(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id)
    skills = models.ResumeSkill.objects.filter(resume=resume)
    print(skills)
    form = forms.ResumeSkillForm()
    if request.method == 'POST':
        form = forms.ResumeSkillForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.ResumeSkillForm()

    return render(request, 'create_resume_skill.html',
                  {'form': form,
                   'skills': skills,
                   'resume_id': resume.id})


def create_resume_experience(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id)
    experiences = models.ResumeExperience.objects.filter(resume=resume)
    print(experiences)
    form = forms.ResumeExperienceForm()
    if request.method == 'POST':
        form = forms.ResumeExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.ResumeExperienceForm()

    return render(request, 'create_resume_experience.html',
                  {'form': form,
                   'experiences': experiences,
                   'resume_id': resume.id})
