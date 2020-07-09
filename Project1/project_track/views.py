from django.contrib.sites.shortcuts import get_current_site
from django.core.serializers import json
from django.forms import model_to_dict
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.contrib.auth import authenticate
# I import login as auth_login so be careful here
from django.contrib.auth import login as auth_login
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from table.views import view_table
from django.contrib.auth.hashers import check_password



from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import *
from .token import reset_password_Generator, account_activation_token
from django.views.generic.base import View

from urllib.parse import quote
from django.utils.encoding import iri_to_uri
#from .models import User
from . import forms
from django.contrib import messages
# from Project1.settings import EMAIL_HOST_USER

from django.conf import settings
from django.core.mail import send_mail
from table.models import PivotFacility
from project_track.models import Sample

from django.http import JsonResponse

from .models import Sample


from .models import Sample
from table.forms import AddDataForms

from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg, Sum, Count, Min, Max, Case, When, F




# Create your views here.

# class User(AbstractUser):
#
#     pass

def home(request):
	# #project_track="I am the project_track application"
	# current_user="Avery Zhang"
	# return render(request, 'home.html',{
	#     'date':datetime.now(),'login':current_user
	# })
	return render(request, 'home.html')


def upload(request):
	if request.method == "POST":
		uploaded_file = request.FILES['document']
		print(uploaded_file.name)
		print(uploaded_file.size)
	return render(request, 'home.html')


def log_in(request):
	# username = request.POST.get('username')
	# password = request.POST.get('password')
	# User.objects.create(username=request.POST.get('username'),
	#                     password=request.POST.get('password'))
	form = forms.UserForm()
	if request.method == "POST":
		message = 'Your email and password did not match. Please try again.'
		try:
			
			form = forms.UserForm(request.POST)
			user_password = request.POST.get('password')
			user_email = request.POST.get('email')
			user = User.objects.get(email=user_email)
			# print("user", user.password)
			user_password_db = user.password
			print(check_password(user_password, user_password_db))
			if check_password(user_password, user_password_db) == True and user.is_active == True:

				user = User.objects.get(email=user_email)
				user.refresh_from_db()
			
				
				facility = Sample.objects.filter(
					Facility_Name=user.profile.facility)[0]
				
				
				request.session['user.profile.facility'] = user.profile.facility
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
				#return render(request, 'table.html', context)
				return redirect(view_table)

			else:

				return render(request, 'login.html', {'message':"User is not yet approved, please try again later."})


			#user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
			# user=authenticate(request, email=user_email, password=request.POST.get('password'))
			# if user.is_authenticated:
			#     # Do something for authenticated users.
			#     print("already authenticated")
			#     #return render(request, 'home.html')
			#     return redirect('../home')
			# else:
			#     # Do something for anonymous users.
			#     print("anonymous")
			#     return render(request, 'login.html')
		except User.DoesNotExist:
			print(request.POST.get('email'), 'does not exist')
			# render to register page
			# user = User.objects.get(user_name=request.POST.get('email'), email=request.POST.get('email'),
			#                                 user_password=request.POST.get('password'))
			# user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
			# authenticate(request, email=request.POST.get('email'), user_password=request.POST.get('password'))
			return render(request, 'login.html', {'form': form, 'message': "User does not exist, please sign up first."})
			# project_track="I am the project_track application"

	else:
		return render(request, 'login.html', {'form': form})


def sign_up(request):

	form = SignUpForm()
	#form = SignUpForm()
	#print(form)
	if request.method == "POST":
		# data = {'first_name':'zhang',
		#           'last_name':'zhang',
		#           'email':'aubrey.lan@outlook.com',
		#           'password1':'111222333zzz',
		#           'password2':'111222333zzz',
		#           'county':'county_C',
		#           'facility':'Avalon Garden'}
		# form = SignUpForm(data)
		# print(form.is_valid())

		form = SignUpForm(request.POST)
		# print(form['county'])
		# print(form['facility'])
		# print(request.POST.get('counties'))
		# print(request.POST.get('facilities'))
		#print(form.cleaned_data)
		if form.is_valid():
			user = form.save(commit=False)
			#user.refresh_from_db()
			user = User.objects.create_user(form)
			# user.profile.first_name = form.cleaned_data.get('first_name')
			# user.profile.last_name = form.cleaned_data.get('last_name')
			# user.profile.county = form.cleaned_data.get('county')
			# user.profile.facility = form.cleaned_data.get('facility')
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.county = form.cleaned_data.get('county')
			user.profile.facility = form.cleaned_data.get('facility')
			user.email = form.cleaned_data.get('email')
			user.set_password(form.cleaned_data.get('password2'))
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
		# user.profile.first_name = request.POST.get('first_name')
		# user.profile.last_name = request.POST.get('last_name')
		# user.profile.county = request.POST.get('counties')
		# user.profile.facility = request.POST.get('facilities')
		# user.first_name = request.POST.get('first_name')
		# user.last_name = request.POST.get('last_name')
		# user.email = request.POST.get('email')
		# user.password = request.POST.get('password2')

		# user can't login until link confirmed
			user.is_active = False
			user.username = user.email
			user.profile.save()
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate Your Account'
			message = render_to_string('account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),
			})
			print(message)
			#user.email_user(subject, message)
			# to_email = form.cleaned_data.get('email')
			to_email = request.POST.get('email')
			email = EmailMessage(subject, message, to=[to_email])
			email.send()
			return redirect('account_activation_sent')

	return render(request, 'signup3.html', {'form': form})


def load_facilities(request):
	user_county = request.GET.get('countyID')
	user_county = user_county.replace("%20", " ")
	if request.is_ajax():
		print("it is Ajax")
	# user_county = request.GET.get('countyID')
	# user_county = "county_B"
	facilities = Sample.objects.filter(County=user_county).values('Facility_Name').order_by('Facility_Name')
	# for item in facilities:
	#     item['name'] = model_to_dict(item['name'])

	#print(list(facilities))
	#choice = forms.ModelChoiceField(queryset=facilities)
	#faci_names = [f for f in facilities]
	#print(faci_names)
	# test_faci = [name['name'] for name in facilities]
	#print(test_faci)
	#facilities = 'Avalon Garden'
	#facilities = Facility.objects.filter(county=user_county)
	data = {
		'facility': list(facilities),
		'error_message':'you have been through this place!!!'
	}
	#print(data)
	return JsonResponse(data)
	#return render(request,'signup3.html', {'facilities': test_faci})


def account_activation_sent(request):
	return render(request, 'account_activation_sent.html')


def monitor(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_confirmed = True

		user.profile.save()
		user.save()
		auth_login(request, user)

		current_site = get_current_site(request)
		subject = 'VOYCE User, Your registration has been approved!!!'
		message = render_to_string('account_success_email.html', {
			'user': user,
			'domain': current_site.domain,
			'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
			'token': account_activation_token.make_token(user),
		})
		#print(message)
		# user.email_user(subject, message)
		# to_email = form.cleaned_data.get('email')
		to_email = user.email
		email = EmailMessage(subject, message, to=[to_email])
		email.send()
		return redirect('login')
	return None


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
		#print(user)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		current_site = get_current_site(request)
		subject = 'VOYCE: New User signed up on Your website, check the new user'
		message = render_to_string('account_monitor_email.html', {
			'user': user,
			'domain': current_site.domain,
			'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
			'token': account_activation_token.make_token(user),
		})
		print(message)
		# user.email_user(subject, message)
		# to_email = form.cleaned_data.get('email')
		#to_email = request.POST.get('email')
		email = EmailMessage(subject, message, to=['nlynch@voycestl.org'])
		email2 = EmailMessage(subject, message, to=['gkwon@voycestl.org'])
		email.send()
		email2.send()
		return redirect('login')
		#context = {'uidb64': uidb64, 'token': token}
	   # return render(request, 'account_activation_email.html', context)
	else:
		messages.warning(
			request, ('The confirmation link was invalid, possibly because it has already been used.'))
		return redirect('signup')


def forget_password(request):
	sub = forms.Subscribe()
	if request.method == 'POST':
		sub = forms.Subscribe(request.POST)
		subject = 'Reset your password'
		user_email = str(sub['email'].value())
		message = 'Please use this link to reset your password. This link will expire in 10 minutes. http://www.voyceconnect.org/reset_password/'
		try:
		# if User.objects.filter(email=user_email).exists():
			user = User.objects.get(email=user_email)
			print(user.pk)
			token = reset_password_Generator.make_token(user)
			#print(User.objects.get(email=user_email))
			recepient = str(sub['email'].value())
			#message =  message + iri_to_uri(quote('/resetpassword/%s' %quote(recepient)))
			message = message  + urlsafe_base64_encode(force_bytes(user.pk)) + '/' + token
			print(message)
			send_mail(subject, message, settings.EMAIL_HOST_USER,
					  [recepient], fail_silently = False)
			return render(request, 'success.html', {'recepient':recepient})
		except User.DoesNotExist:
			#print(sub.errors)
			return render(request, 'forgetpsd.html', {'form': sub, "message":'Your email does not exist. Please sign up first.'})
	return render(request, 'forgetpsd.html', {'form': sub})


def reset_password(request):
	form = forms.PassReset()
	if request.method == "POST":
		form = forms.PassReset(request.POST)
		email = request.POST.get('email')
		user_password = request.POST.get('user_password')
		user_password_conf = request.POST.get('user_password_confirm')

		if user_password == user_password_conf:
			user_object = User.objects.get(email=email)
			user_object.refresh_from_db()
			user_object.profile.email_confirmed = True
			user_object.set_password(user_password_conf)
			#user_object.profile_user.save()
			user_object.save()
			return render(request, 'reset_success.html', {"message": 'Password reset, please log in again'})
		return render(request, 'reset_password.html', {'form': form})
	return render(request, 'reset_password.html', {'form': form})


class ResetPasswordView(View):
	def get(self, request, uidb64, token):
		try:
			uid = force_text(urlsafe_base64_decode(uidb64))
			print(uid)
			user = User.objects.get(pk=uid)

		except (TypeError, ValueError, OverflowError, User.DoesNotExist):
			user = None
			print('user problem')
		#user is not None and
		if reset_password_Generator.check_token(user, token):
			# user.profile.email_confirmed = True
			# user.save()
			# login(request, user)
			# return redirect('reset_password.html')
			print('finally succeed')
			return redirect('/reset_password/')
			# return render(request, 'reset_password.html')
		else:
			# invalid link
			print("invalid link")
			return render(request, 'test.html')

def test(request):

	print(request.GET.get('countyID'))
	return render(request, 'signup.html')

def dashboard_view(request):
    ds = PivotDataPool(
        series=[
            {'options': {
                'source': Sample.objects.annotate(sumbed=F('Open_Female_Medicaid_Beds')+F('Open_Male_Medicaid_Beds')+F('Open_Female_Medicare_Beds')+F('Open_Male_Medicare_Beds')+F('Open_Female_Private_Pay_Beds')+F('Open_Male_Private_Pay_Beds')+F('Open_Female_Dementia_Beds')+F('Open_Male_Dementia_Beds'), summedicaid=F('Open_Female_Medicaid_Beds')+F('Open_Male_Medicaid_Beds')),
                # Sample.objects.raw('SELECT Open_Female_Medicaid_Beds + Open_Male_Medicaid_Beds + Open_Female_Medicare_Beds+Open_Male_Medicare_Beds+Open_Female_Private_Pay_Beds+Open_Male_Private_Pay_Beds+Open_Female_Dementia_Beds+Open_Male_Dementia_Beds AS sumbed,Open_Female_Medicaid_Beds+Open_Male_Dementia_Beds AS summedicaid from Sample'),
                'categories': 'County'

            },

                'terms': {
                    'Total Bed': Sum('sumbed'), 'Total Medicaid Bed': Sum('summedicaid'),
                    # 'legend_by':['Region'],
            }
            }])
    pivcht = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'
                # #type: 'bar' vertical x
            },
                'terms': ['Total Bed', 'Total Medicaid Bed'],
            }],
        chart_options={
            'title': {
                'text': 'Total Bed vs. Medicaid Bed'
            },
            'subtitle': {
                'text': 'Across County',
            },
            'xAxis': {
                'title': {'text': 'County'}},
            'yAxis': {
                'title': {'text': 'Number of Beds'}},
            'legend': {
                'layout': 'vertical',
                'align': 'right',
                'verticalAlign': 'center',
                'x': -10,
                'y': 30,  # smaller y, higher legend
                'floating': True,
                'borderWidth': 1,
                "backgroundColor": '#EEEEEE',
                'shadow': True,
                'reversed': True
            },
            'plotOptions': {
                'column': {  # if 'bar', not control column type, no label
                    'dataLabels': {
                        'enabled': True
                    },
                    'pointPadding': 0,
                    'borderWidth': 4,  # larger width, slimmer bar
                    'borderRadius': 1
                }}, })

    return render(request, 'dashboard.html', {'pivotlist': [pivcht]})

