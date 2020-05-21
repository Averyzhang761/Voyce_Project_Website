from django.contrib.auth.models import User
from django.db import models
import django.shortcuts
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
import pymysql as Database
Database.install_as_MySQLdb()

# Create your models here.

FACILITY_CHOICES = (
    ('Avalon Garden', 'Avalon Garden'),
    ('Baisch Nursing Center', 'Baisch Nursing Center'),
    ('Ballwin Ridge Health and Rehab', 'Ballwin Ridge Health and Rehab'),
    ('Big River Nursing and Rehab', 'Big River Nursing and Rehab'),
    ('Chestnut Rehab and Nursing', 'Chestnut Rehab and Nursing'),
    ('Community Care Center of Lemay', 'Community Care Center of Lemay'),
    ('Cori Manor', 'Cori Manor'),
    ('Country Aire', 'Country Aire'),
    ('Crystal Oaks', 'Crystal Oaks'),
    ('Delhaven Manor', 'Delhaven Manor'),
    ('Delmar Gardens of Creve Coeur', 'Delmar Gardens of Creve Coeur'),
    ('Dolan Memory Care Homes', 'Dolan Memory Care Homes'),
    ('Elsberry Health Care Center', 'Elsberry Health Care Center'),
    ('Fountainbleau NC', 'Fountainbleau NC'),
    ('Frontier Health and Rehab', 'Frontier Health and Rehab'),
    ('Gamma Road Lodge', 'Gamma Road Lodge'),
    ('Gerald Nursing and Rehab', 'Gerald Nursing and Rehab'),
    ('Glenfield Memory Care Home', 'Glenfield Memory Care Home'),
    ('Laclede Groves', 'Laclede Groves'),
    ('Life Care Center of Sullivan', 'Life Care Center of Sullivan'),
    ('Maple Grove Lodge', 'Maple Grove Lodge'),
    ('Moberly Nursing and Rehab', 'Moberly Nursing and Rehab'),
    ("Ms. B's Blessings", "Ms. B's Blessings"),
    ('Nazareth Living Center', 'Nazareth Living Center'),
    ('NHC Maryland Heights', 'NHC Maryland Heights'),
    ('Oak Pointe of Warrenton', 'Oak Pointe of Warrenton'),
    ('Pacific Care Center', 'Pacific Care Center'),
    ('Provision Living', 'Provision Living'),
    ('Scenic Nursing and Rehab', 'Scenic Nursing and Rehab'),
    ('Smiley Manor RCF', 'Smiley Manor RCF'),
    ('St. Louis Altenheim', 'St. Louis Altenheim'),
    ('St. Clair Nursing Center', 'St. Clair Nursing Center'),
    ('St. Peters Manor', 'St. Peters Manor'),
    ('St. Sophia Health and Rehab', 'St. Sophia Health and Rehab'),
    ('Sunrise Senior Living of Webster Groves',
     'Sunrise Senior Living of Webster Groves'),
    ('Sylvan House', 'Sylvan House'),
    ('The Boarding Inn', 'The Boarding Inn'),
    ('Union Manor RCF', 'Union Manor RCF'),
    ('Windsor Estates of St. Charles', 'Windsor Estates of St. Charles')
)


'''
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)
    facility = models.CharField(
        max_length=100, choices=FACILITY_CHOICES, default='Avalon Garden')
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
