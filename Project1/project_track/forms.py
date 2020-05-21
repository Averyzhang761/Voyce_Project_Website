from django.forms import ModelForm
from django import forms
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


FACILITY_CHOICES = (
    ('Avalon Garden', 'Avalon Garden'),
    ('Baisch Nursing Center', 'Baisch Nursing Center'),
    ('Ballwin Ridge Health and Rehab', 'Ballwin Ridge Health and Rehab'),
    ('Big River Nursing and Rehab', 'Big River Nursing and Rehab'),
    ('Chestnut Rehab and Nursing', 'Chestnut Rehab and Nursing'),
    ('Community Care Center of Lemay', 'Community Care Center of Lemay'),
    ('Cori Manor', 'Cori Manor'),
    ('Country Aire', 'Country Aire'),
    ('Crystal Oaks', 'Crystal Oaks'),
    ('Delhaven Manor', 'Delhaven Manor'),
    ('Delmar Gardens of Creve Coeur', 'Delmar Gardens of Creve Coeur'),
    ('Dolan Memory Care Homes', 'Dolan Memory Care Homes'),
    ('Elsberry Health Care Center', 'Elsberry Health Care Center'),
    ('Fountainbleau NC', 'Fountainbleau NC'),
    ('Frontier Health and Rehab', 'Frontier Health and Rehab'),
    ('Gamma Road Lodge', 'Gamma Road Lodge'),
    ('Gerald Nursing and Rehab', 'Gerald Nursing and Rehab'),
    ('Glenfield Memory Care Home', 'Glenfield Memory Care Home'),
    ('Laclede Groves', 'Laclede Groves'),
    ('Life Care Center of Sullivan', 'Life Care Center of Sullivan'),
    ('Maple Grove Lodge', 'Maple Grove Lodge'),
    ('Moberly Nursing and Rehab', 'Moberly Nursing and Rehab'),
    ("Ms. B's Blessings", "Ms. B's Blessings"),
    ('Nazareth Living Center', 'Nazareth Living Center'),
    ('NHC Maryland Heights', 'NHC Maryland Heights'),
    ('Oak Pointe of Warrenton', 'Oak Pointe of Warrenton'),
    ('Pacific Care Center', 'Pacific Care Center'),
    ('Provision Living', 'Provision Living'),
    ('Scenic Nursing and Rehab', 'Scenic Nursing and Rehab'),
    ('Smiley Manor RCF', 'Smiley Manor RCF'),
    ('St. Louis Altenheim', 'St. Louis Altenheim'),
    ('St. Clair Nursing Center', 'St. Clair Nursing Center'),
    ('St. Peters Manor', 'St. Peters Manor'),
    ('St. Sophia Health and Rehab', 'St. Sophia Health and Rehab'),
    ('Sunrise Senior Living of Webster Groves',
     'Sunrise Senior Living of Webster Groves'),
    ('Sylvan House', 'Sylvan House'),
    ('The Boarding Inn', 'The Boarding Inn'),
    ('Union Manor RCF', 'Union Manor RCF'),
    ('Windsor Estates of St. Charles', 'Windsor Estates of St. Charles')
)

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
