from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('upload/', views.upload, name='upload'),
    #path('signup/', views.signup, name="signup"),
    #path('signup/', views.CreateFacilityView.as_view(), name="signup"),
    path('signup/', views.signup, name='signup'),
    path('test/', views.test, name="test"),
    path('sent/', views.account_activation_sent,
        name='account_activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('forgetpsd/', views.forgetpsd, name='forgetpsd'),
    path('reset/', views.resetpsd, name='resetpsd'),

]
