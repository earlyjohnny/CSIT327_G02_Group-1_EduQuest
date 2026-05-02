from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('login/',    views.login_view,        name='login'),
    path('logout/',   views.logout_view,       name='logout'),

    # Session-protected pages
    path('home/',     views.home_view,         name='home'),
    path('profile/',  views.edit_profile_view, name='edit_profile'),
    path('record/',   views.add_record_view,   name='add_record'),

    # Public event list  ← this now handles events/
    path('',          views.event_list,        name='event_list'),
]