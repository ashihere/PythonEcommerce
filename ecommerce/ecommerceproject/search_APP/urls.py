from django.urls import path
from . import views

app_name="search_APP"
urlpatterns=[
    path('',views.searchResult,name='searchResult'),
]