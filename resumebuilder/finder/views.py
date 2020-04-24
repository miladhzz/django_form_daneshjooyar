from django.shortcuts import render
from . import forms
from . import models


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print("welcome {}".format(form.cleaned_data['name']))
            form.save()
    return render(request, 'contact.html', {'form': form})
