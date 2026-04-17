from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegistrationsView.as_view(), name='registrations_index'),
    path('addNewRegistration/', views.AddRegistrationView.as_view(), name='add_registration'),
]