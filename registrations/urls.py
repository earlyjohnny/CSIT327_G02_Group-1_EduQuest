from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.RegistrationsHomeView.as_view(), name='registrations_home'),
    path('registration/', views.RegistrationsIndexView.as_view(), name='registrations_index'),
    path('attendance/', views.AttendanceIndexView.as_view(), name='attendance_index'),
    path('addNewRegistration/', views.AddRegistrationView.as_view(), name='add_registration'),
    path('addNewAttendance/', views.AddAttendanceView.as_view(), name='add_attendance'),
    path('editprofile/', views.EditProfileView.as_view(), name='registrations_editprofile'),
    path('logout/', views.RegistrationsLogoutView.as_view(), name='registrations_logout'),
]