from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Facility, PivotFacility
from .forms import AddDataForms
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
import os
import csv


def index(request):
    return render(request, 'index.html')


def view_table(request):
    facility = Facility.objects.filter(name=request.user.profile_user.facility)[0]
    female_medicaid = facility.female_medicaid
    male_medicaid = facility.male_medicaid
    female_medicare = facility.female_medicare
    male_medicare = facility.male_medicare
    female_private = facility.female_private
    male_private = facility.male_private
    female_dementia = facility.female_dementia
    male_dementia = facility.male_dementia
    female = PivotFacility.objects.create(gender='female',
                                          medicaid=female_medicaid,
                                          medicare=female_medicare,
                                          private=female_private,
                                          dementia=female_dementia)
    male = PivotFacility.objects.create(gender='male',
                                        medicaid=male_medicaid,
                                        medicare=male_medicare,
                                        private=male_private,
                                        dementia=male_dementia)

    context = {
        'female': female,
        'male': male,
        'facility': facility,
    }
    return render(request, 'table.html', context)
