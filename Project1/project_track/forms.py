from table.models import Facility
from django.forms import ModelForm
from django import forms
from .models import User

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'table')))

# Create your models here.

names = Facility.objects.values('name')
facilities = [name['name'] for name in names]

FACILITY_CHOICES = tuple([(facility, facility) for facility in facilities])


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    facility = forms.ChoiceField(choices=FACILITY_CHOICES)
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User

        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'facility')

    User._meta.get_field('email')._unique = True


class UserForm(forms.Form):
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # users = forms.CharField(label='User_name',
    #                         widget=forms.Select(choices=user_list))
    class Meta:
        model = User
        fields = ['user_city','user_facility','user_name','first_name','last_name','email']


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user_name'].queryset = User.objects.none()

class Subscribe(forms.Form):
    email = forms.EmailField()

    def _str_(self):
        return self.email

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # if User.objects.filter(email=email).exists():
        #     raise forms.ValidationError("This email address is not registered, please sign up first.")
        return email


    User._meta.get_field('email')._unique = True



class PassReset(forms.Form):
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # users = forms.CharField(label='User_name',
    #                         widget=forms.Select(choices=user_list))
    #fields = ['user_city','user_facility','user_name','first_name','last_name','email']
    email = forms.CharField(max_length=60)
    user_password = forms.CharField(max_length=60)
    user_password_confirm = forms.CharField(max_length=60)

