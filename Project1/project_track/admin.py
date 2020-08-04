from django.contrib.admin.helpers import ActionForm
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
import csv
from django.http import HttpResponse

from .models import Info

from .models import Sample

from .filters import DropdownFilter

admin.site.site_header = 'VOYCE Admin Management Console'

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected"
    
class InfoAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ["Facility_Name",
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
                    "Google_Review_Page", ]
    list_display_links = ["Facility_Name"]
    list_filter = (("Facility_Name", DropdownFilter),
                   ("Type", DropdownFilter),
                   ("County", DropdownFilter),
                   ("City", DropdownFilter),
                   ("Accept_New_Residents", DropdownFilter),
                   ("Number_of_Beds", DropdownFilter),
                   ("Age_Limit", DropdownFilter),
                   ("Memory_Care", DropdownFilter),
                   ("Behavior_or_Psych_Unit", DropdownFilter),
                   ("Pay_Medicaid", DropdownFilter),
                   ("Pay_Medicaid_Pending", DropdownFilter),
                   ("Pay_Medicare", DropdownFilter),
                   ("Pay_DMH", DropdownFilter),
                   ("Pay_Private_Pay", DropdownFilter),
                   ("Accept_Quadriplegic_and_Paraplegic", DropdownFilter),
                   ("Accept_Patients_with_Chemical_Dependence_History",
                    DropdownFilter),
                   ("Hearing_Impairment_Accommodation", DropdownFilter),
                   ("Visual_Impairment_Accommodation", DropdownFilter),
                   ("Wound_Care", DropdownFilter),
                   ("Wander_Guard", DropdownFilter),
                   ("VA_Contracts", DropdownFilter),
                   ("Accept_Chemical_Dependence", DropdownFilter),
                   ("Respite_Care", DropdownFilter),
                   ("Coma", DropdownFilter),
                   ("Bariatric_Care", DropdownFilter),
                   ("IV_Therapy", DropdownFilter),
                   ("Trach_Tube", DropdownFilter),
                   ("Dialysis", DropdownFilter),
                   ("Ventilator", DropdownFilter),
                   ("Accept_COVID_Patients", DropdownFilter)
                   )
    search_fields = ["Facility_Name"]
    actions = ["export_as_csv"]
    
    def get_queryset(self, request):
        queryset = super(InfoAdmin, self).get_queryset(request)
        queryset = queryset.order_by("Facility_Name")
        return queryset



class SampleAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ["Facility_Name", "County", "Timestamp", "Open_Female_Medicaid_Beds",
                    "Open_Male_Medicaid_Beds", "Open_Female_Medicare_Beds",
                    "Open_Male_Medicare_Beds", "Open_Female_Private_Pay_Beds",
                    "Open_Male_Private_Pay_Beds", "Open_Female_Dementia_Beds",
                    "Open_Male_Dementia_Beds"]
#     list_editable = ["Open_Female_Medicaid_Beds",
#                      "Open_Male_Medicaid_Beds", "Open_Female_Medicare_Beds",
#                      "Open_Male_Medicare_Beds", "Open_Female_Private_Pay_Beds",
#                      "Open_Male_Private_Pay_Beds", "Open_Female_Dementia_Beds",
#                      "Open_Male_Dementia_Beds"]
    list_display_links = ["Facility_Name"]
    list_filter = (("Facility_Name", DropdownFilter),
                   "Timestamp", ("County", DropdownFilter))
    search_fields = ["Facility_Name"]
    actions = ["export_as_csv"]
#     def has_add_permission(self, request):
#         return False
    class UpdateActionForm(ActionForm):
       Facility_Name = forms.CharField(required=False)
    def ReplaceFN(modeladmin, request, queryset):
        myDict = dict(request.POST.lists())
        queryset.update(Facility_Name=myDict["Facility_Name"][0])
    ReplaceFN.short_description = "Replace Facility Name"
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
# admin.site.register(All,AllAdmin)
# admin.site.unregister(Group)
