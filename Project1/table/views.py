from django.shortcuts import render
from table.models import Table
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

	with open('../Project1/voyce.csv') as csvfile:

		next(csvfile)

		data = csv.reader(csvfile, delimiter=',')

		for items in data:


			facility = items[0]
			type = items[1]

			number_beds = items[2]
			region = items[3]
			address = items[4]
			city = items[5]
			state = items[6]
			zip = items[7]
			telefone = items[8]
			fax = items[9]
			admin = items[10]
			admin_email = items[11]
			sw = items[12]
			sw_email = items[13]
			markt = items[14]
			markt_email = items[15]

			user = Table.objects.get_or_create(facility=facility,
				type=type,
				number_beds=number_beds,
				region=region,
				address=address,
				city=city,
				state=state,
				zip=zip,
				telefone=telefone,
				fax=fax,
				admin=admin,
				admin_email=admin_email,
				sw=sw,
				sw_email=sw_email,
				markt=markt,
				markt_email=markt_email
				)
	users = Table.objects.all()

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
	model = Table
	template_name = 'searchresults.html'

	def get_queryset(self):

		queryset = self.request.GET.get('q')
		objects = Table.objects.filter(
			Q(facility__icontains=queryset))

		return objects


