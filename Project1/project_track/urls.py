import patterns as patterns
from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.login, name="login"),
    path('home/',views.home, name="home"),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.signup, name="signup"),
    path('test/', views.test, name="test"),
    path('forgetpsd/', views.forgetpsd, name='forgetpsd'),
    # (r'^r/', include('urlcrypt.urls')),
    path('reset_password/', views.resetpsd, name='resetpsd'),
    url(r'^reset_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                views.ResetPasswordView.as_view(), name='password_reset'),

    # url(r'^reset_password/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #             views.ResetPasswordView.as_view(), name='password_reset'),
]

