from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.models import User

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.core.mail import EmailMessage




#from .models import User
from .models import Sample

# Create your views here.


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


def login(request):

    if request.method == "POST":
        try:

            email = request.POST.get('email')
            password = request.POST.get('password')
            user_object = User.objects.get(
                email=email, password=password)
            context = {"objects": user_object}
            return render(request, 'welcome.html', context)

        except User.DoesNotExist:
            print(request.POST.get('email'), 'does not exist')

            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def signup(request):

    form = SignUpForm(request.POST)

    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.facility = form.cleaned_data.get('facility')        
        # user can't login until link confirmed
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        subject = 'Activate Your Account'
        message = render_to_string('account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        #user.email_user(subject, message)
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(subject, message, to=[to_email])
        email.send()
        return redirect('account_activation_sent')

    return render(request, 'signup3.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        auth_login(request, user)
        return redirect('login')
        #context = {'uidb64': uidb64, 'token': token}
       # return render(request, 'account_activation_email.html', context)
    else:
        messages.warning(
            request, ('The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('signup')

'''
def signup(request):

    if request.method == "POST":
        form = FacilityForm(request.POST)
     
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('email')
        user_password = request.POST.get('user_password')
        facility = request.POST.get('facility')
        
        print('success')
        object = User.objects.create(user_name=user_name, first_name=first_name, last_name=last_name,
                                     email=user_email, user_password=user_password, facility=facility)
        
        context = {"objects": object}
        return render(request, 'welcome.html', context)
    else:
        return render(request, 'signup.html')
'''


def test(request):
    # objects, created=User.objects.get_or_create(user_id=2, user_name = 'archt', first_name = 'arch', last_name = 'talents',
    #  email = 'arch@talentu', user_password = '12345678')
    # if created:
    #     print('new instance')
    #     # , user_name = 'avery61', first_name = 'Avery', last_name = 'Zhang',
    #     # email = 'lanxi.z@wustl.edu', user_password = '12345678
    #     # objects.set_user_name('archt')
    #     # objects.set_first_name('arch')
    #     # objects.set_last_name('talents')
    #     # objects.set_email('arch@talents')
    #     # objects.set_user_password('archtt121')
    #     # objects.save()
    #     print(created)
    #     objects.user_name='archt'
    #     objects.first_name='arch'
    #     objects.last_name='talents'
    #     objects.email='arch@talents'
    #     objects.user_password='12345678'
    #     objects.save()
    # User.objects.create()
    #query_results = objects

    # objects = User.objects.create(user_id=2, user_name='archt', first_name='arch', last_name='talents',
    #                                        email = 'arch@talentu', user_password = '12345678')
    # objects=User.objects.get(user_id=2)
    # objects.delete()
    # objects=User.objects.get(user_name='jamesz')
    objects = User.objects.all().values
    context = {"objects": objects}

    print(context)
    return render(request, 'welcome.html', context)
