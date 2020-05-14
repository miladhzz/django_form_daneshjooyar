from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from creator import models


@login_required
def generate_resume(request):
    resume = get_object_or_404(models.Resume, user=request.user)
    print(resume.id)
    resume_skills = models.ResumeSkill.objects.filter(resume=resume)
    resume_educations = models.ResumeEducation.objects.filter(resume=resume)
    resume_experiences = models.ResumeExperience.objects.filter(resume=resume)
    return render(request, 'generate_resume.html', {'resume': resume,
                                                    'resume_skills': resume_skills,
                                                    'resume_educations': resume_educations,
                                                    'resume_experiences': resume_experiences})

