from django import forms
from .models import Table



class AddDataForms(forms.ModelForm):
	class Meta:
		model = Table
		fields = ["facility", "type", "number_beds", 'region',
		'address', 'city', 'state', 'zip', 'telefone', 'fax', 'admin',
		'admin_email', 'sw', 'sw_email', 'markt', 'markt_email']
