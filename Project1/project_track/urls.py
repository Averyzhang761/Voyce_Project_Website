from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns=[
    path('',views.log_in, name="login"),
    path('home/',views.home, name="home"),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.sign_up, name="signup"),
    path('test/', views.test, name="test"),
    path('sent/', views.account_activation_sent,
         name='account_activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('monitor/<slug:uidb64>/<slug:token>/',
         views.monitor, name='monitor'),
    path('forgetpsd/', views.forget_password, name='forgetpsd'),
    path('reset/', views.reset_password, name='resetpsd'),
    # (r'^r/', include('urlcrypt.urls')),
    path('reset_password/', views.reset_password, name='resetpsd'),

    url(r'^reset_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                views.ResetPasswordView.as_view(), name='password_reset'),
    path('ajax/load-facilities/', views.load_facilities, name='ajax_load_facilities'),  # <-- this one here

]
