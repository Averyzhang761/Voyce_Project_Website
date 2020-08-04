from django import forms
from project_track.models import Sample, Info


class AddDataForms(forms.ModelForm):
    class Meta:
        model = Sample
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
        model = Info
        fields = ["County",
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
                  "Pay_Medicaid",
                  "Pay_Medicaid_Pending",
                  "Pay_Medicare",
                  "Pay_DMH",
                  "Pay_Private_Pay",
                  "VA_Contracts",
                  "Accept_Quadriplegic_and_Paraplegic",
                  "Accept_Patients_with_Chemical_Dependence_History",
                  "Accept_Chemical_Dependence",
                  "Hearing_Impairment_Accommodation",
                  "Visual_Impairment_Accommodation",
                  "Wound_Care",
                  "Wander_Guard",
                  "Respite_Care",
                  "Coma",
                  "Bariatric_Care",
                  "IV_Therapy",
                  "Trach_Tube",
                  "Ventilator",
                  "Dialysis",
                  "Notes",
                  "Accept_COVID_Patients",
                  "Facility_Website",
                  "Facility_Facebook",
                  "Nursing_Home_Compare",
                  "Google_Review_Page",]
