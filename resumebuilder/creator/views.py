from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from . import models
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView


# @login_required
# def create_resume(request):
#     form = forms.ResumeForm()
#     if request.method == 'POST':
#         form = forms.ResumeForm(request.POST, request.FILES)
#         if form.is_valid():
#             resume = form.save(commit=False)
#             resume.user = request.user
#             resume.name = request.user.first_name
#             resume.family = request.user.last_name
#             resume.save()
#             return HttpResponseRedirect(reverse('creator:edit_resume', args=(resume.id, )))
#     return render(request, 'create_resume.html', {'form': form})

class CreateResume(LoginRequiredMixin, CreateView):
    form_class = forms.ResumeForm
    template_name = 'create_resume.html'

    def get_success_url(self):
        return reverse('creator:edit_resume', args=(self.object.id, ))

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.name = self.request.user.first_name
        form.instance.family = self.request.user.last_name
        return super().form_valid(form)

@login_required()
def edit_resume(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id)
    form = forms.ResumeForm(instance=resume)
    return render(request, 'create_resume.html', {'form': form})


@login_required()
def create_resume_education(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id)
    educations = models.ResumeEducation.objects.filter(resume=resume)
    print(educations)
    form = forms.ResumeEducationForm()
    if request.method == 'POST':
        form = forms.ResumeEducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.resume = resume
            education.save()
            form = forms.ResumeEducationForm()

    return render(request, 'create_resume_education.html',
                  {'form': form,
                   'educations': educations,
                   'resume_id': resume.id})


@login_required()
def create_resume_skill(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id)
    skills = models.ResumeSkill.objects.filter(resume=resume)
    print(skills)
    resume_skill_formset = formset_factory(forms.ResumeSkillForm, extra=3)
    formset = resume_skill_formset()
    if request.method == 'POST':
        formset = resume_skill_formset(request.POST)
        if formset.is_valid():
            for form in formset:
                skill = form.save(commit=False)
                skill.resume = resume
                skill.save()
                formset = resume_skill_formset()

    return render(request, 'create_resume_skill.html',
                  {'formset': formset,
                   'skills': skills,
                   'resume_id': resume.id})


@login_required()
def create_resume_experience(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id)
    experiences = models.ResumeExperience.objects.filter(resume=resume)
    print(experiences)
    form = forms.ResumeExperienceForm()
    if request.method == 'POST':
        form = forms.ResumeExperienceForm(request.POST)
        if form.is_valid():
            print("form is valid")
            experience = form.save(commit=False)
            experience.resume = resume
            experience.save()
            form = forms.ResumeExperienceForm()

    return render(request, 'create_resume_experience.html',
                  {'form': form,
                   'experiences': experiences,
                   'resume_id': resume.id})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('creator:login'))
    return render(request, 'registration/register.html', {'form': form})


@login_required()
def view_profile(request):
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})


@login_required()
def edit_profile(request):
    form = forms.EditProfileForm(instance=request.user)
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('creator:profile'))
    return render(request, 'registration/edit_profile.html', {'form': form})


@login_required()
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('creator:profile'))
    return render(request, 'registration/change_password.html', {'form': form})
