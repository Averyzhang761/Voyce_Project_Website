from project_track.models import Sample
from django.forms import ModelForm
from django import forms
#from .models import User

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'table')))

# Create your models here.

names = Sample.objects.values('Facility_Name')
facilities = [name['Facility_Name'] for name in names]
county_names = Sample.objects.values('County')
print(type(county_names))
#counties = list(set(county_names['county']))
counties = [name['County'] for name in county_names]
uniqu_counties = list(set(counties))
#uniqu_counties = ['County_A','County_B']
#counties = uniqu_counties
COUNTY_CHOICE = tuple([(county, county) for county in uniqu_counties])
FACILITY_CHOICES = tuple([(facility, facility) for facility in facilities])

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    county = forms.ChoiceField(widget = forms.Select, choices=COUNTY_CHOICE, required=True)
    facility = forms.ChoiceField(widget = forms.Select, choices=FACILITY_CHOICES, required=True)
    
    # queryset=Add_Site.objects.order_by('subnet').values_list('subnet', flat=True).distinct()
    # facility = forms.ChoiceField(choices=FACILITY_CHOICES)
    # county = forms.ModelChoiceField(
    #     queryset=Country.objects.all(),
    #     label=u"Country",
    #     widget=ModelSelect2Widget(
    #         model=Country,
    #         search_fields=['name__icontains'],
    #     )
    # )
    #
    # facility = forms.ModelChoiceField(
    #     queryset=City.objects.all(),
    #     label=u"City",
    #     widget=ModelSelect2Widget(
    #         model=City,
    #         search_fields=['name__icontains'],
    #         dependent_fields={'country': 'country'},
    #         max_results=500,
    #     )
    # )
    email = forms.EmailField(
        max_length=254, help_text='Please provide a valid email address.')

    class Meta:
        model = User

        fields = ('first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'county',
                  'facility')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['county'].queryset = Facility.objects.values('county').all()
        # self.fields['facility'].queryset = Facility.objects.all().distinct()


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

