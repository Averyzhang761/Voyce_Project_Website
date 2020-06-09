from django import forms
from .models import Facility, All


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


class AddAllForms(forms.ModelForm):
    class Meta:
        model = All
        fields =["Facility_Name",
                "Type",
                "County",
                "Address",
                "City",
                "State",
                "Zipcode",
                "Telephone",
                "Fax",
                "Admin",
                "Admin_Email",
                "Social_Worker",
                "SW_Email",
                "Markt_or_Admission",
                "Markt_or_Admission_Email",
                "Accept_New_Residents",
                "Number_of_Beds",
                "Age_Limit",
                "Memory_Care",
                "Behavior_or_Psych_Unit",
                "Payments",
                "Accept_Quadriplegic_and_Paraplegic",
                "Accept_Patients_with_Chemical_Dependence_History",
                "Accept_Chemical_Dependence",
                "Hearing_Impairment_Accommodation",
                "Visual_Impairment_Accommodation",
                "Wound_Care",
                "Wander_Guard",
                "VA_Contracts",
                "Respite_Care",
                "Coma",
                "Bariatric_Care",
                "IV_Therapy",
                "Trach_Tube_or_Ventilator",
                "Dialysis",
                "Notes",
                "Accept_COVID_Patients"]
