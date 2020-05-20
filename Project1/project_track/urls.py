from django.urls import path
from . import views

urlpatterns=[
    path('',views.login, name="login"),
    path('home/',views.home, name="home"),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.signup, name="signup"),
    #path('forgetpsd/', views.test, name='forgetpsd'),
    path('forgetpsd/', views.forgetpsd, name='forgetpsd'),
    path('reset/', views.resetpsd, name='resetpsd'),
    path('test/', views.test, name="test"),

    # path('test2/', views.UserListView.as_view(), name='person_changelist'),
    # path('add/', views.UserCreateView.as_view(), name='person_add'),
    # path(r'^facture/modifier/<int:pk>/$', views.UserUpdateView.as_view(), name='person_change'),
    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
