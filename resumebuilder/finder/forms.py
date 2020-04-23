from django import forms


attr = {'class': 'form-control'}


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=attr),
                           max_length=20, min_length=5,
                           error_messages={
                               'required': 'Please enter name',
                               'min_length': 'نام وارد شده کوتاه است',
                               'max_length': 'The name is long.'
                           })
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
