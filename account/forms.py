from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import ugettext_lazy as _


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(required=True, max_length=30,
                                 label='First Name',
                                 widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Prénom'),
                                          'autofocus': 'autofocus'}))
    last_name = forms.CharField(required=True, max_length=30,
                                label='Last Name',
                                widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Nom'),
                                          'autofocus': 'autofocus'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ChangeProfile(forms.Form):
    first_name = forms.CharField(required=True, max_length=30,
                                 label='First Name',
                                 widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Prénom'),
                                          'autofocus': 'autofocus'}))
    last_name = forms.CharField(required=True, max_length=30,
                                label='Last Name',
                                widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Nom'),
                                          'autofocus': 'autofocus'}))

    def save(self, user):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        user.first_name = first_name
        user.last_name = last_name
        user.save()
