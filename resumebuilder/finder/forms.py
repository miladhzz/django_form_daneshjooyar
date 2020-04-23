from django import forms
from django.core import validators


attr = {'class': 'form-control'}


def check_name_length(value):
    if len(value) > 10:
        raise forms.ValidationError("The name is long.")


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=attr),
                           validators=[check_name_length])
    family = forms.CharField(widget=forms.TextInput(attrs=attr))
    email = forms.EmailField(widget=forms.EmailInput(attrs=attr))
    retype_email = forms.EmailField(widget=forms.EmailInput(attrs=attr))
    message = forms.CharField(widget=forms.Textarea(attrs=attr))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        retype_email = cleaned_data.get('retype_email')

        if email != retype_email:
            raise forms.ValidationError("email and retype email is not equal !")
