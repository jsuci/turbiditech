# forms
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm

# models
from .models import CustomUser, Device, Component


class LoginForm(ModelForm):
    class Meta:
        model   = CustomUser
        fields  = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['password'].widget.attrs.update({'autocomplete': 'email'})
        self.fields['password'].widget.attrs.update({'class': 'input'})
        self.fields['password'].widget.attrs.update({'autocomplete': 'current-password'})
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


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input'})


class ResetPasswordConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'input'})
        self.fields['new_password2'].widget.attrs.update({'class': 'input'})

# use same AddDeviceForm to update device 
class AddDeviceForm(ModelForm):
    class Meta:
        model       = Device
        fields      = ['device_name', 'location', 'install_date', 'install_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device_name'].widget.attrs.update({'class': 'input'})
        self.fields['location'].widget.attrs.update({'class': 'input'})
        self.fields['install_date'].widget.attrs.update({'class': 'input'})
        self.fields['install_date'].widget.input_type = 'date'
        self.fields['install_time'].widget.attrs.update({'class': 'input'})
        self.fields['install_time'].widget.input_type = 'time'


# use same AddComponentForm to update component 
class AddComponentForm(ModelForm):
    class Meta:
        model       = Component
        fields      = ['component_name', 'device_link', 'install_date', 'install_time', 'installed_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['component_name'].widget.attrs.update({'class': 'input'})
        self.fields['install_date'].widget.attrs.update({'class': 'input'})
        self.fields['install_date'].widget.input_type = 'date'
        self.fields['installed_by'].widget.attrs.update({'class': 'input'})
        self.fields['install_time'].widget.attrs.update({'class': 'input'})
        self.fields['install_time'].widget.input_type = 'time'
