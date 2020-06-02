from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.update_data, name='new'),
    path('table/', views.view_table, name='view_table'),
    path('searchresults/', views.SearchResultsView.as_view(), name='searchresults')
    ]
