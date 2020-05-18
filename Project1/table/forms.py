from django import forms
from .models import Facility


class AddDataForms(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ["name",
                  "date",
                  "female_medicaid",
                  "male_medicaid",
                  "female_medicare",
                  "male_medicare",
                  "female_private",
                  "male_private",
                  "female_dementia",
                  "male_dementia",
                  "notes",
                  ]
