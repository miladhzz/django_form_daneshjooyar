from django import forms


attr = {'class': 'form-control'}


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=attr), max_length=5)
    family = forms.CharField(widget=forms.TextInput(attrs=attr))
    email = forms.EmailField(widget=forms.EmailInput(attrs=attr))
    message = forms.CharField(widget=forms.Textarea(attrs=attr))
