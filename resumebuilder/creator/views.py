from django.shortcuts import render


def create_resume(request):
    return render(request, 'create_resume.html')
