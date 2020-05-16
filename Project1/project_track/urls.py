from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.login, name="login"),
    path('home/',views.home, name="home"),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.signup, name="signup"),
    path('test/', views.test, name="test"),
]
