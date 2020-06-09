# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contact(models.Model):
    PURPOSE_CHOICES = [
        ('IN', 'Inquiry'),
        ('CO', 'Complaint'),
        ('FB', 'Feedback'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    purpose = models.CharField(max_length=2, choices=PURPOSE_CHOICES)
    message = models.TextField()
class Facility(models.Model):
    # county = models.CharField(max_length=100,null=False)
    name = models.CharField(max_length=100, null=False)
    county = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=30, blank=True, null=False)
    female_medicaid = models.SmallIntegerField(blank=True)
    male_medicaid = models.SmallIntegerField(blank=True)
    female_medicare = models.SmallIntegerField(blank=True)
    male_medicare = models.SmallIntegerField(blank=True)
    female_private = models.SmallIntegerField(blank=True)
    male_private = models.SmallIntegerField(blank=True)
    female_dementia = models.SmallIntegerField(blank=True)
    male_dementia = models.SmallIntegerField(blank=True)
    notes = models.TextField(blank=True, null=False)


    class Meta:
        managed = False
        db_table = 'facility'


class PivotFacility(models.Model):
    gender = models.CharField(max_length=10)
    medicaid = models.SmallIntegerField()
    medicare = models.SmallIntegerField(blank=True, null=True)
    private = models.SmallIntegerField(blank=True, null=True)
    dementia = models.SmallIntegerField(blank=True, null=True)



class All(models.Model):
    Facility_Name = models.CharField(
        unique=False, db_index=False, primary_key=True, auto_created=False, max_length=50)
    Type = models.CharField(max_length=20)
    County = models.CharField(max_length=50)
    Address = models.CharField(max_length=200, blank=True)
    City = models.CharField(max_length=50, blank=True)
    State = models.CharField(max_length=30, blank=True)
    Zipcode = models.CharField(max_length=30, blank=True)
    Telephone = models.CharField(max_length=20, blank=True)
    Fax = models.CharField(max_length=20, blank=True)
    Admin = models.CharField(max_length=50, blank=True)
    Admin_Email = models.CharField(max_length=50, blank=True)
    Social_Worker = models.CharField(max_length=50, blank=True)
    SW_Email = models.CharField(max_length=50, blank=True)
    Markt_or_Admission = models.CharField(max_length=50, blank=True)
    Markt_or_Admission_Email = models.CharField(max_length=50, blank=True)
    Accept_New_Residents = models.CharField(max_length=50, blank=True)
    Number_of_Beds = models.IntegerField(max_length=3, blank=True)
    Age_Limit = models.IntegerField(max_length=3, blank=True)
    Memory_Care = models.CharField(max_length=50, blank=True)
    Behavior_or_Psych_Unit = models.CharField(max_length=50, blank=True)
    Payments = models.CharField(max_length=20, blank=True)
    Accept_Quadriplegic_and_Paraplegic = models.CharField(
        max_length=50, blank=True)
    Accept_Patients_with_Chemical_Dependence_History = models.CharField(
        max_length=50, blank=True)
    Accept_Chemical_Dependence = models.CharField(max_length=50, blank=True)
    Hearing_Impairment_Accommodation = models.CharField(
        max_length=50, blank=True)
    Visual_Impairment_Accommodation = models.CharField(
        max_length=50, blank=True)
    Wound_Care = models.CharField(max_length=50, blank=True)
    Wander_Guard = models.CharField(max_length=50, blank=True)
    VA_Contracts = models.CharField(max_length=50, blank=True)
    Respite_Care = models.CharField(max_length=50, blank=True)
    Coma = models.CharField(max_length=50, blank=True)
    Bariatric_Care = models.CharField(max_length=50, blank=True)
    IV_Therapy = models.CharField(max_length=50, blank=True)
    Trach_Tube_or_Ventilator = models.CharField(max_length=50, blank=True)
    Dialysis = models.CharField(max_length=30, blank=True)
    Notes = models.CharField(max_length=200, blank=True)
    Accept_COVID_Patients = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.Facility_Name + ' ' + self.County + ' ' + self.Type

    class Meta:
        managed = False 
        db_table = 'project_track_info'
