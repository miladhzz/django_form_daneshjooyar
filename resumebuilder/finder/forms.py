from django import forms


attr = {'class': 'form-control'}


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=attr))
    family = forms.CharField(widget=forms.TextInput(attrs=attr))
    email = forms.EmailField(widget=forms.EmailInput(attrs=attr))
    message = forms.CharField(widget=forms.Textarea(attrs=attr))

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 10:
            raise forms.ValidationError("The name is long.")
        return name
