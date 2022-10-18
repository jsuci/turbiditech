# forms
from django import forms
from django.forms import ModelForm, EmailInput, PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm

# models
from .models import CustomUser


class LoginForm(ModelForm):
    class Meta:
        model   = CustomUser
        fields  = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['password'].widget.attrs.update({'class': 'input'})
        self.fields['password'].widget.input_type = 'password'

class RegisterForm(UserCreationForm):

    # add eamil field since USerCreationForm does not have one
    email = forms.EmailField(max_length=60, help_text='A valid email address is required.')

    class Meta:
        model   = CustomUser
        fields  = ['first_name', 'last_name', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'input'})
        self.fields['last_name'].widget.attrs.update({'class': 'input'})
        self.fields['email'].widget.attrs.update({'class': 'input', 'type': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'input', 'type': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'input', 'type': 'password'})


    # custom form validation before
    # this will run when form is submitted
    # error messages are also displayed through ValidationError
    # clean_<your field name> is the naming convention
    
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            CustomUser.objects.get(email__iexact=email)
            raise forms.ValidationError('Email already exists')
        except CustomUser.DoesNotExist:
            return email

    def clean_password2(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')
        if pw1 and pw2 and pw1 == pw2:
            return pw2
        raise forms.ValidationError("Passwords do not match")