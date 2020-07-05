from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import django.shortcuts
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
import pymysql as Database
from datetime import datetime



import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'table')))
Database.install_as_MySQLdb()

# Create your models here.


class Sample(models.Model):
        def number():
        no = Sample.objects.latest('id')
        no = no.id
        if no == None:
            return 1
        else:
            return no + 1

    id = models.IntegerField(unique=True, primary_key=True,default=number)
    #id = models.AutoField(unique=True, primary_key=True)
    Facility_Name = models.CharField(unique=False, db_index=False, auto_created=False, max_length=50)
    County = models.CharField(max_length=50)
    Timestamp = models.DateTimeField(max_length=50, auto_now_add=True)
    #Timestamp = models.CharField(max_length=50)
    #As_of = models.CharField(max_length=50)
    Open_Female_Medicaid_Beds = models.IntegerField(blank=True)
    Open_Male_Medicaid_Beds = models.IntegerField(blank=True)
    Open_Female_Medicare_Beds = models.IntegerField(blank=True)
    Open_Male_Medicare_Beds = models.IntegerField(blank=True)
    Open_Female_Private_Pay_Beds = models.IntegerField(blank=True)
    Open_Male_Private_Pay_Beds = models.IntegerField(blank=True)
    Open_Female_Dementia_Beds = models.IntegerField(blank=True)
    Open_Male_Dementia_Beds = models.IntegerField( blank=True)
    Notes = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.Facility_Name + ' ' + self.County + ' '
    class Meta:
        db_table = 'project_track_sample'
        # Add verbose name
        verbose_name = 'Facility_bed_information'


names = Sample.objects.values('Facility_Name')
facilities = [name['Facility_Name'] for name in names]

FACILITY_CHOICES = tuple([(facility, facility) for facility in facilities])


class Info(models.Model):
    Facility_Name = models.CharField(
        unique=False, db_index=False, primary_key=True, auto_created=False, max_length=50)
    Type = models.CharField(max_length=20)
    County = models.CharField(max_length=50)
    #Sub_Type = models.CharField(max_length=20, blank=True)
    Address = models.CharField(max_length=200, blank=True)
    City = models.CharField(max_length=50, blank=True)
    State = models.CharField(max_length=30, blank=True)
    Zipcode = models.IntegerField(blank=True)
    Telephone = models.CharField(max_length=20, blank=True)
    Fax = models.CharField(max_length=20, blank=True)
    Admin = models.CharField(max_length=50, blank=True)
    Admin_Email = models.CharField(max_length=50, blank=True)
    Social_Worker = models.CharField(max_length=50, blank=True)
    SW_Email = models.CharField(max_length=50, blank=True)
    Markt_or_Admission = models.CharField(max_length=50, blank=True)
    Markt_or_Admission_Email = models.CharField(max_length=50, blank=True)
    Number_of_Beds = models.IntegerField(blank=True)
    Accept_New_Residents = models.CharField(max_length=50, blank=True)
    Age_Limit = models.IntegerField(blank=True)
    Memory_Care = models.CharField(max_length=50, blank=True)
    Behavior_or_Psych_Unit = models.CharField(max_length=50, blank=True)
    Pay_Medicaid = models.CharField(max_length=50, blank=True)
    Pay_Medicaid_Pending = models.CharField(max_length=50, blank=True)
    Pay_Medicare = models.CharField(max_length=50, blank=True)
    Pay_DMH = models.CharField(max_length=50, blank=True)
    Pay_Private_Pay = models.CharField(max_length=50, blank=True)
    VA_Contracts = models.CharField(max_length=50, blank=True)
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
    Respite_Care = models.CharField(max_length=50, blank=True)
    Coma = models.CharField(max_length=50, blank=True)
    Bariatric_Care = models.CharField(max_length=50, blank=True)
    IV_Therapy = models.CharField(max_length=50, blank=True)
    Trach_Tube = models.CharField(max_length=50, blank=True)
    Ventilator = models.CharField(max_length=50, blank=True)
    Dialysis = models.CharField(max_length=50, blank=True)
    Notes = models.CharField(max_length=200, blank=True)
    Accept_COVID_Patients = models.CharField(max_length=50, blank=True)
    Facility_Website =  models.CharField(
        max_length=100, blank=True)
    Facility_Facebook = models.CharField(
        max_length=100, blank=True)
    DHSS_Page = models.CharField(
        max_length=100, blank=True)
    Nursing_Home_Compare = models.CharField(
        max_length=100, blank=True)
    Google_Review_Page = models.CharField(
        max_length=100, blank=True)

    def __unicode__(self):
        return self.Facility_Name + ' ' + self.County + ' ' + self.Type
    class Meta:
        db_table = 'project_track_info'
        # Add verbose name
        verbose_name = 'Facility_Attribute'

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100)
    facility = models.CharField(max_length=100)
    email_confirmed = models.BooleanField(default=False)

    class Meta:
        managed = False

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    # instance.profile.save()

#
# class Test(models.Model):
#     user_id = models.IntegerField(
#         unique=True, db_index=True, primary_key=True, auto_created=True)
#     user_name = models.CharField(max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=60)
#     user_password = models.CharField(max_length=60)


