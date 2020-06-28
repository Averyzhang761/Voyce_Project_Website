from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
#     path('', views.index, name="index"),
    path('new/', views.update_data, name='new'),
    path('table/', views.view_table, name='view_table'),
    path('..', views.back_to_log_in, name='back_login'),
    path('searchresults/', views.SearchResultsView.as_view(), name='searchresults'),
    path('extension/', views.view_all, name='extension'),
    path('newextension/', views.update_all, name='newextension')
    ]
