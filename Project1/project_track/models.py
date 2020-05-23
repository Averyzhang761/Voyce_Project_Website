from django.contrib.auth.models import User
from django.db import models
import django.shortcuts
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
import pymysql as Database

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'table')))
from table.models import Facility
Database.install_as_MySQLdb()

# Create your models here.

names = Facility.objects.values('name')
facilities = [name['name'] for name in names]

FACILITY_CHOICES = tuple([(facility, facility) for facility in facilities])


'''
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_city = models.CharField(max_length=60, default="Saint Louis")
    user_facility = models.CharField(max_length=100, default="Facility 1")
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)
    facility = models.CharField(
        max_length=100, choices=FACILITY_CHOICES, default='Avalon Garden')
'''
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile_user")
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    facility = models.CharField(max_length=60)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Test(models.Model):
    user_id = models.IntegerField(
        unique=True, db_index=True, primary_key=True, auto_created=True)
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)


class Sample(models.Model):
    Facility_Name = models.CharField(
        unique=True, db_index=False, primary_key=True, auto_created=False, max_length=45)
    As_of = models.DateField()
    Open_Female_Medicaid_Beds = models.IntegerField()
    Open_Male_Medicaid_Beds = models.IntegerField()
    Open_Female_Medicare_Beds = models.IntegerField()
    Open_Male_Medicare_Beds = models.IntegerField()
    Open_Female_Private_Pay_Beds = models.IntegerField()
    Open_Male_Private_Pay_Beds = models.IntegerField()
    Open_Female_Dementia_Beds = models.IntegerField()
    Open_Male_Dementia_Beds = models.IntegerField()
    Notes = models.CharField(max_length=200)

    def __unicode__(self):
        return self.Facility_Name
