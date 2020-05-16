from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User

from .models import User
# Create your views here.
def home(request):
    # #project_track="I am the project_track application"
    # current_user="Avery Zhang"
    # return render(request, 'home.html',{
    #     'date':datetime.now(),'login':current_user
    # })
    return render(request, 'home.html')

def upload(request):
    if request.method=="POST":
        uploaded_file=request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'home.html')

def login(request):
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # User.objects.create(username=request.POST.get('username'),
    #                     password=request.POST.get('password'))
    if request.method=="POST":
        try:

            user_email=request.POST.get('email')
            user_password=request.POST.get('password')
            user_object = User.objects.get(email=user_email, user_password=user_password)
            context = {"objects": user_object}
            # login(request)
            return render(request, 'welcome.html', context)
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
            #render to register page
            # user = User.objects.get(user_name=request.POST.get('email'), email=request.POST.get('email'),
            #                                 user_password=request.POST.get('password'))
            # user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            # authenticate(request, email=request.POST.get('email'), user_password=request.POST.get('password'))
            return render(request, 'login.html')
            # project_track="I am the project_track application"

    else:
        return render(request, 'login.html')

def signup(request):
    # #project_track="I am the project_track application"
    # current_user="Avery Zhang"
    # return render(request, 'home .html',{
    #     'date':datetime.now(),'login':current_user
    # })
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password_confirmation')
        print('success')
        object=User.objects.create(user_name=user_name, first_name=first_name, last_name=last_name,
                                   email=user_email, user_password=user_password)
        context = {"objects": object}
        return render(request, 'welcome.html', context)
    else:
        return render(request, 'signup.html')
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
    context={"objects":objects}

    print(context)
    return render(request, 'welcome.html',context)
