from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('events/addNewEvent/', views.add_new_event, name='add_new_event'),
    path('events/addNewVenue/', views.add_new_venue, name='add_new_venue'),
]