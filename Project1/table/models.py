# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=30, blank=True, null=True)
    female_medicaid = models.SmallIntegerField()
    male_medicaid = models.SmallIntegerField(blank=True, null=True)
    female_medicare = models.SmallIntegerField(blank=True, null=True)
    male_medicare = models.SmallIntegerField(blank=True, null=True)
    female_private = models.SmallIntegerField(blank=True, null=True)
    male_private = models.SmallIntegerField(blank=True, null=True)
    female_dementia = models.SmallIntegerField(blank=True, null=True)
    male_dementia = models.SmallIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility'

class PivotFacility(models.Model):
    gender = models.CharField(max_length=10)
    medicaid = models.SmallIntegerField()
    medicare = models.SmallIntegerField(blank=True, null=True)
    private = models.SmallIntegerField(blank=True, null=True)
    dementia = models.SmallIntegerField(blank=True, null=True)