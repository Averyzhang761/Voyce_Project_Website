from django.shortcuts import render
from django.contrib.auth.models import User
from .models import PivotFacility
from project_track.models import Sample, Info
from .forms import AddDataForms, AddAllForms
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, UpdateView
from django.db.models import Q
from django.shortcuts import get_object_or_404
import os
import csv
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def back_to_log_in(request):
	return render(request, "login.html")

def index(request):
	return render(request, 'index.html')
# Create your views here.
# request is HttpRequestObject that is created whenever a page is loaded
# render looks for HTML templates inside a directory called templates


def view_table(request):

	facility = Sample.objects.filter(
		Facility_Name=request.session['user.profile.facility'])[0]
	female_medicaid = facility.Open_Female_Medicaid_Beds
	male_medicaid = facility.Open_Male_Medicaid_Beds
	female_medicare = facility.Open_Female_Medicare_Beds
	male_medicare = facility.Open_Male_Medicare_Beds
	female_private = facility.Open_Female_Private_Pay_Beds
	male_private = facility.Open_Male_Private_Pay_Beds
	female_dementia = facility.Open_Female_Dementia_Beds
	male_dementia = facility.Open_Male_Dementia_Beds
	female = PivotFacility.objects.create(gender='Female',
									   medicaid=female_medicaid,
									   medicare=female_medicare,
									   private=female_private,
									   dementia=female_dementia)
	male = PivotFacility.objects.create(gender='Male',
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


def update_data(request):
	
	n = len(Sample.objects.all())
	print('len', n)
	facility = Sample.objects.filter(
		Facility_Name=request.session['user.profile.facility'])[0]

	form = AddDataForms(instance=facility)
	#instance=facility

	success_url = reverse_lazy('view_table')

	if "cancel" in request.POST:

		return HttpResponseRedirect(success_url)

	if request.method == 'POST':
		form = AddDataForms(request.POST)

		if form.is_valid():
			female_medicaid = form.cleaned_data.get('Open_Female_Medicaid_Beds')
			male_medicaid = form.cleaned_data.get('Open_Male_Medicaid_Beds')
			female_medicare = form.cleaned_data.get('Open_Male_Medicare_Beds')
			male_medicare = form.cleaned_data.get('Open_Male_Medicare_Beds')
			female_private = form.cleaned_data.get('Open_Female_Private_Pay_Beds')
			male_private = form.cleaned_data.get('Open_Male_Private_Pay_Beds')
			female_dementia = form.cleaned_data.get('Open_Female_Dementia_Beds')
			male_dementia = form.cleaned_data.get('Open_Male_Dementia_Beds')

			newsample = Sample.objects.create(
                            id=facility.id - facility.id + n+1,
							Facility_Name=facility.Facility_Name,
							County=facility.County,
							Open_Female_Medicaid_Beds=female_medicaid,
							Open_Male_Medicaid_Beds=male_medicaid,
							Open_Female_Medicare_Beds=female_medicare,
							Open_Male_Medicare_Beds=male_medicare,
							Open_Female_Private_Pay_Beds=female_private,
							Open_Male_Private_Pay_Beds=male_private,
							Open_Female_Dementia_Beds=female_dementia,
							Open_Male_Dementia_Beds=male_dementia,
			)
			newsample.save()
			return redirect('view_table')

		return redirect('view_table')

	context = {
		'form': form,
		'facility': facility
	}

	return render(request, 'newdata.html', context)


def view_all(request):

	#fields = All._meta.get_fields()
	#
	#facility = All.objects.values()
	#
	#for item in facility:
	#	if item['Facility_Name'] == request.session['user.profile.facility']:
	#			target = item
	#			break
	#
	#values = list(target.values())
	#
	#zipvalues = zip(fields, values)

	facility = Info.objects.filter(
		Facility_Name=request.session['user.profile.facility'])[0]

	context = {
			'facility': facility,
	}

	return render(request, 'viewall.html', context)


def update_all(request):

	facility = Info.objects.filter(
		Facility_Name=request.session['user.profile.facility'])[0]

	form = AddAllForms(instance=facility)

	#zipvalues = zip(fields, values)

	success_url = reverse_lazy('view_all')

	if "cancel" in request.POST:

		return redirect('extension')

	if request.method == 'POST':
		form = AddAllForms(request.POST, instance=facility)

		if form.is_valid():
			form.save()

			return redirect('extension')

		return redirect('extension')

	context = {
		'form': form,
		'facility': facility
	}

	return render(request, 'edit_all.html', context)


class SearchResultsView(ListView):
	model = Sample
	template_name = 'searchresults.html'

	def get_queryset(self):

		queryset = self.request.GET.get('q')
		objects = Sample.objects.filter(
			Q(facility__icontains=queryset))

		return objects

