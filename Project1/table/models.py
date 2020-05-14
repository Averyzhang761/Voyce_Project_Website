from django.db import models

# Class attributes correspond to columns 
# Instances of the classes correspond to rows in the database. 

# Create your models here.
class Table(models.Model):
	facility = models.CharField(max_length=200, blank=True, null=True)
	type = models.CharField(max_length=20, blank=True, null=True)
	number_beds = models.CharField(max_length=20, blank=True, null=True)
	region = models.CharField(max_length=100, blank=True, null=True)
	address = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	state = models.CharField(max_length=5, blank=True, null=True)
	zip = models.CharField(max_length=20, blank=True, null=True)
	telefone = models.CharField(max_length=200, blank=True, null=True)
	fax = models.CharField(max_length=200, blank=True, null=True)
	admin = models.CharField(max_length=200, blank=True, null=True)
	admin_email = models.EmailField(blank=True, null=True)
	sw = models.CharField(max_length=200, blank=True, null=True)
	sw_email = models.EmailField(blank=True, null=True)
	markt = models.CharField(max_length=200, blank=True, null=True)
	markt_email = models.EmailField(blank=True, null=True)



