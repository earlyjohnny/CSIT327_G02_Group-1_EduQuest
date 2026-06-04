from django.urls import path
from . import views

app_name = 'organizations'
urlpatterns = [
    path('organizations/', views.HomeView.as_view(), name='index'),
    path('organizations/addNewOrganization', views.AddOrganizationView.as_view(), name='addNewOrganization'),
    path('', views.LoginView.as_view(), name='login'),
    path('home/', views.DashboardView.as_view(), name='home_page'),
    path('edit-profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('logoff/', views.LogoutView.as_view(), name='logoff'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('add-category/', views.AddCategoryView.as_view(), name='add_category'),
]
