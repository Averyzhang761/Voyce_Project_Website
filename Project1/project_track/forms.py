from django import forms
from .models import User

# user_list= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]


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

