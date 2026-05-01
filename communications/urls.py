from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_redirect, name='communications_root'),
    path('login/', views.login_view, name='communications_login'),
    path('register/', views.register_view, name='communications_register'),
    path('logout/', views.logout_view, name='communications_logout'),
    path('home/', views.home, name='communications_home'),
    path('edit-profile/', views.edit_profile, name='communications_edit_profile'),
    path('addNewAnnouncement/', views.add_announcement, name='add_announcement'),
    path('index/', views.index, name='communications_index'),
]