from django.urls import path
from . import views

app_name = 'organizations'
urlpatterns = [
    path('organizations/', views.HomeView.as_view(), name='index'),
    path('organizations/addNewOrganization', views.AddOrganizationView.as_view(), name='addNewOrganization'),
    path('', views.home, name='login'),
    path('home/', views.home_page, name='home_page'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('add-record/', views.add_record, name='add_record'),
    path('logoff/', views.logoff, name='logoff'),
    path('register/', views.register, name='register'),
    path('add-category/', views.add_category, name='add_category'),
]
