from table.models import Facility
from django.forms import ModelForm
from django import forms
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'table')))
Database.install_as_MySQLdb()

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
    
    '''
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email exists")
        return self.cleaned_data
    '''


    User._meta.get_field('email')._unique = True
