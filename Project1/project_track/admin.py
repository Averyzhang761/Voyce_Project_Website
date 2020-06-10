from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

from .models import Info

from .models import Sample

from .filters import DropdownFilter

admin.site.site_header = 'VOYCE Admin Management Console'


class InfoAdmin(admin.ModelAdmin):
    list_display = ["Facility_Name", "County", "Type",
                    "Address", "City", "State", "Zipcode", "Telephone", "Fax", "Admin",
                    "Admin_Email",  # "Social_Worker","SW_Email","Markt_or_Admission",
                    #"Markt_or_Admission_Email",
                    "Accept_New_Residents", "Age_Limit"]

    #["Memory_Care",
    #"Behavior_or_Psych_Unit","Payments","Accept_Quadriplegic_and_Paraplegic",
    #"Accept_Patients_with_Chemical_Dependence_History","Hearing_Impairment_Accommodation",
    #"Visual_Impairment_Accommodation","Wound_Care","Wander_Guard","VA_Contracts",
    #"Accept_Chemical_Dependence","Respite_Care","Coma","Bariatric_Care","IV_Therapy",
    #"Trach_Tube_or_Ventilator","Dialysis","Notes","Accept_COVID_Patients"]
    list_display_links = ["Facility_Name"]
    list_filter = (("Facility_Name", DropdownFilter), ("Type", DropdownFilter), ("County", DropdownFilter),
                   ("City", DropdownFilter), ("Accept_New_Residents", DropdownFilter), ("Admin", DropdownFilter), ("Age_Limit", DropdownFilter))
    search_fields = ["Facility_Name"]

    def get_queryset(self, request):
        queryset = super(InfoAdmin, self).get_queryset(request)
        queryset = queryset.order_by("Facility_Name")
        return queryset


class SampleAdmin(admin.ModelAdmin):
    list_display = ["Facility_Name", "County", "Timestamp", "As_of", "Open_Female_Medicaid_Beds",
                    "Open_Male_Medicaid_Beds", "Open_Female_Medicare_Beds",
                    "Open_Male_Medicare_Beds", "Open_Female_Private_Pay_Beds",
                    "Open_Male_Private_Pay_Beds", "Open_Female_Dementia_Beds",
                    "Open_Male_Dementia_Beds"]
    list_editable = ["As_of", "Open_Female_Medicaid_Beds",
                     "Open_Male_Medicaid_Beds", "Open_Female_Medicare_Beds",
                     "Open_Male_Medicare_Beds", "Open_Female_Private_Pay_Beds",
                     "Open_Male_Private_Pay_Beds", "Open_Female_Dementia_Beds",
                     "Open_Male_Dementia_Beds"]
    list_display_links = ["Facility_Name"]
    list_filter = (("Facility_Name", DropdownFilter),
                   "Timestamp", ("County", DropdownFilter))
    search_fields = ["Facility_Name"]

    def get_queryset(self, request):
        queryset = super(SampleAdmin, self).get_queryset(request)
        queryset = queryset.order_by("Facility_Name")
        return queryset

# class AllAdmin(admin.ModelAdmin):
#
#     list_display = ["Facility_Name","County","Type","Sub_Type","Number_of_Beds",
#                     "Address","City","State","Telephone","Fax","Admin",
#                     "Admin_Email","Social_Worker","SW_Email","Markt_or_Admission",
#                     "Markt_or_Admission_Email","Age_Limit","Memory_Care",
#                     "Behavior_or_Psych_Unit","Payments","Accept_Quadriplegic_and_Paraplegic",
#                     "Accept_Patients_with_Chemical_Dependence_History","Hearing_Impairment_Accommodation",
#                     "Visual_Impairment_Accommodation","Wound_Care","Wander_Guard","VA_Contracts",
#                     "Accept_Chemical_Dependence","Respite_Care","Coma","Bariatric_Care","IV_Therapy",
#                     "Trach_Tube_or_Ventilator","Dialysis","Notes_1"]
#     list_display_links = ["Facility_Name"]
#     form = AllForm
#     list_filter = ["Facility_Name","County","Type"]
#     search_fields = ["Facility_Name"]
#     def get_queryset(self, request):
#         queryset = super(AllAdmin, self).get_queryset(request)
#         queryset = queryset.order_by("Facility_Name")
#         return queryset


admin.site.register(Info, InfoAdmin)
admin.site.register(Sample, SampleAdmin)
#admin.site.register(All,AllAdmin)
# admin.site.unregister(Group)
