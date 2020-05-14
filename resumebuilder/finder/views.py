from django.shortcuts import render
from . import forms
from creator import models
from django.db.models import Count


def index(request):
    genders = models.Sex.objects.all()
    skills = models.Skill.objects.all()
    educations = models.Education.objects.all()

    resume_list = models.Resume.objects.all()

    # name
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            resume_list = resume_list.filter(name__istartswith=name)

    # family
    if 'family' in request.GET:
        family = request.GET['family']
        if family:
            resume_list = resume_list.filter(family__istartswith=family)

    # age
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            resume_list = resume_list.filter(age__lte=int(age))

    # gender
    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            resume_list = resume_list.filter(sex=int(gender))

    # education
    if 'education' in request.GET:
        education = request.GET['education']
        if education:
            resume_list = resume_list.distinct().filter(resume_education__education=int(education))

    # skill
    if 'skill' in request.GET:
        skill = request.GET['skill']
        if skill:
            resume_list = resume_list.distinct().filter(resume_skill__skill=int(skill))

    # company-count
    if 'company_count' in request.GET:
        company_count = request.GET['company_count']
        if company_count:
            resume_list = resume_list.annotate(exp_count=
                                               Count('resume_experience')).filter(exp_count__gte=int(company_count))

    # working-now
    if 'working_now' in request.GET:
        working_now = request.GET['working_now']
        working_now = check_working_now(working_now)
        resume_list = resume_list.distinct().filter(resume_experience__working_now=working_now)

    print(resume_list)

    search_param = request.GET

    return render(request, 'index.html', {'genders': genders,
                                          'skills': skills,
                                          'educations': educations,
                                          'resume_list': resume_list,
                                          'search_param': search_param})


def check_working_now(val):
    try:
        return {
            '1': True,
            '0': False,
            '-1': None,
        }[val]
    except KeyError:
        return False


def contact(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print("welcome {}".format(form.cleaned_data['name']))
            form.save()
    return render(request, 'contact.html', {'form': form})
