from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    is_staff = forms.BooleanField(required=True)
    is_superuser = forms.BooleanField(required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_staff = self.cleaned_data['is_staff']
        user.is_superuser = self.cleaned_data['is_superuser']
        user.save()

        return user
