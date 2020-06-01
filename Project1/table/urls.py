from django.urls import path
#from table import views
#
#urlpatterns = [
#	path('new/', views.add_data, name='new'),
#	path('searchresults/', views.SearchResultsView.as_view(), name='searchresults')
#	]

from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.add_data, name='new'),
    path('searchresults/', views.SearchResultsView.as_view(), name='searchresults')
]
