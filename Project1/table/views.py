from django.shortcuts import render
from table.models import Facility
from .forms import AddDataForms
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
import os
import csv


# Create your views here.
# request is HttpRequestObject that is created whenever a page is loaded
# render looks for HTML templates inside a directory called templates

def view_table(request):

	users = Facility.objects.all()

	context = {
		'users': users
	}
	return render(request, 'table.html', context)

def add_data(request):
	form = AddDataForms()
	if request.method == 'POST':
		form = AddDataForms(request.POST)
		if form.is_valid():
			form.save()

			return redirect('view_table')
	#users1 = Table.objects.all()
	context = {
		#'users': users1,
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


