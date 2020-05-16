from django.db import models
import django.shortcuts
from django.shortcuts import render
import pymysql as Database
Database.install_as_MySQLdb()

from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user_id=models.IntegerField(unique=True, db_index=True, primary_key=True, auto_created=True)
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)

class Sample(models.Model):
    Facility_Name=models.CharField(unique=True, db_index=False, primary_key=True, auto_created=False, max_length=45)
    As_of = models.DateField(max_length=30)
    Open_Female_Medicaid_Beds = models.IntegerField(max_length=11)
    Open_Male_Medicaid_Beds = models.IntegerField(max_length=11)
    Open_Female_Medicare_Beds = models.IntegerField(max_length=11)
    Open_Male_Medicare_Beds = models.IntegerField(max_length=11)
    Open_Female_Private_Pay_Beds = models.IntegerField(max_length=11)
    Open_Male_Private_Pay_Beds = models.IntegerField(max_length=11)
    Open_Female_Dementia_Beds = models.IntegerField(max_length=11)
    Open_Male_Dementia_Beds = models.IntegerField(max_length=11)
    Notes=models.CharField(max_length=200)

    def __unicode__(self):
        return self.Facility_Name

