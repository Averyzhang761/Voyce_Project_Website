from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Facility, PivotFacility
from .forms import AddDataForms
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
import os
import csv


# Create your views here.
# request is HttpRequestObject that is created whenever a page is loaded
# render looks for HTML templates inside a directory called templates

# def view_table(request):
#
# 	# users = Facility.objects.all()
# 	#facility = Facility.objects.filter(name=request.user.profile_user.facility)[0]
# 	print(Facility.objects.all())
# 	#user = User.objects.get(email=request.POST.get('email'))
# 	print(request.session.get("email"))
# 	#print(request.POST.get('email'))
# 	facility = Facility.objects.filter(name=request.user.profile.facility)[0]
# 	female_medicaid = facility.female_medicaid
# 	male_medicaid = facility.male_medicaid
# 	female_medicare = facility.female_medicare
# 	male_medicare = facility.male_medicare
# 	female_private = facility.female_private
# 	male_private = facility.male_private
# 	female_dementia = facility.female_dementia
# 	male_dementia = facility.male_dementia
# 	female = PivotFacility.objects.create(gender='female',
#                                        medicaid=female_medicaid,
#                                        medicare=female_medicare,
#                                        private=female_private,
#                                        dementia=female_dementia)
# 	male = PivotFacility.objects.create(gender='male',
#                                      medicaid=male_medicaid,
#                                      medicare=male_medicare,
#                                      private=male_private,
#                                      dementia=male_dementia)
#
# 	context = {
# 		'female': female,
# 		'male': male,
# 		'facility': facility,
# 	}
# 	return render(request, 'table.html', context)


def add_data(request):
	form = AddDataForms()
	if request.method == 'POST':
		form = AddDataForms(request.POST)
		if form.is_valid():
			form.save()

			return redirect('view_table')
	# users1 = Table.objects.all()
	context = {
		# 'users': users1,
		'form': form,
	}

	return render(request, 'newdata.html', context)


class SearchView(TemplateView):
    template_name = 'table.html'


class SearchResultsView(ListView):
	model = Facility
	template_name = 'searchresults.html'

	def get_queryset(self):

		queryset = self.request.GET.get('q')
		objects = Facility.objects.filter(
			Q(facility__icontains=queryset))

		return objects

