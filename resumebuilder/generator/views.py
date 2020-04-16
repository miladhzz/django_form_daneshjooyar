from django.shortcuts import render


def generate_resume(request):
    return render(request, 'generate_resume.html')

