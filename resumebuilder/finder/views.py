from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = forms.ContactForm()
    return render(request, 'contact.html', {'form': form})
