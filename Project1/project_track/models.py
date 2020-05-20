from django.db import models
import django.shortcuts
from django.shortcuts import render
import pymysql as Database
Database.install_as_MySQLdb()
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user_id=models.IntegerField(unique=True, db_index=True, primary_key=True, auto_created=True)
    user_city = models.CharField(max_length=60, default="Saint Louis")
    user_facility = models.CharField(max_length=100, default="Facility 1")
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)


class Test(models.Model):
    user_id=models.IntegerField(unique=True, db_index=True, primary_key=True, auto_created=True)
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)
