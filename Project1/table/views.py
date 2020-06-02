from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Facility, PivotFacility
from .forms import AddDataForms
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, UpdateView
from django.db.models import Q
from django.shortcuts import get_object_or_404
import os
import csv
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy



def index(request):
	return render(request, 'index.html')
# Create your views here.
# request is HttpRequestObject that is created whenever a page is loaded
# render looks for HTML templates inside a directory called templates


def view_table(request):

	facility = Facility.objects.filter(name=request.user.profile.facility)[0]
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
	
	

def update_data(request):
	facility=Facility.objects.filter(name=request.user.profile.facility)[0]

	form=AddDataForms(instance=facility)

	success_url = reverse_lazy('view_table')

	if "cancel" in request.POST:
		
		return HttpResponseRedirect(success_url)

	if request.method == 'POST':
		form=AddDataForms(request.POST, instance=facility)

		if form.is_valid():
			form.save()

			return redirect('view_table')
		

		return redirect('view_table')

	context={
		'form': form,
		'facility': facility
	}

	return render(request, 'newdata.html', context)



def add_data(request):
	form=AddDataForms()
	if request.method == 'POST':
		form=AddDataForms(request.POST)
		if form.is_valid():
			form.save()

			return redirect('view_table')
	# users1 = Table.objects.all()
	context={
		# 'users': users1,
		'form': form,
	}

	return render(request, 'newdata.html', context)

#class SearchView(TemplateView):
#	template_name='table.html'
#
#
#
class SearchResultsView(ListView):
	model=Facility
	template_name='searchresults.html'

	def get_queryset(self):

		queryset=self.request.GET.get('q')
		objects=Facility.objects.filter(
			Q(facility__icontains=queryset))

		return objects
