from django import forms
from .models import Facility


class AddDataForms(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ["Open_Female_Medicaid_Beds",
                  "Open_Male_Medicaid_Beds",
                  "Open_Female_Medicare_Beds",
                  "Open_Male_Medicare_Beds",
                  "Open_Female_Private_Pay_Beds",
                  "Open_Male_Private_Pay_Beds",
                  "Open_Female_Dementia_Beds",
                  "Open_Male_Dementia_Beds",
                  "Notes",
                  ]

    

