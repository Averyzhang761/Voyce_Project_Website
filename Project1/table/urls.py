from django.urls import path
from table import views

urlpatterns = [
	path('new/', views.add_data, name='new'),
	path('searchresults/', views.SearchResultsView.as_view(), name='searchresults')
	]