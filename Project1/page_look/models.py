from django.db import models

# Create your models here.
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