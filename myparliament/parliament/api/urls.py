from django.urls import path
from . import views


app_name = 'parliament'

urlpatterns = [
    path('list/',
         views.ParliamentListView.as_view(),
         name='mps_list'),
    path('list&pp=<str>/',
         views.ParliamentListView.as_view(),
         name='mps_list'),
    path('list&dob=<str>/',
         views.ParliamentListView.as_view(),
         name='mps_list'),
    path('mp/<pk>/',
         views.ParliamentDetailView.as_view(),
         name='mp_detail'),
    path('search/',
         views.ParliamentSearchListView.as_view(),
         name='mps_search'),
]
