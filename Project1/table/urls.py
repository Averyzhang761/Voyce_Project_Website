from django.urls import path
from table import views

urlpatterns = [
	path('table/', views.view_table, name='view_table'),
	path('new/', views.add_data, name='new'),
	path('searchresults/', views.SearchResultsView.as_view(), name='searchresults')
	]