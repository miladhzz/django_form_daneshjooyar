from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    family = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
