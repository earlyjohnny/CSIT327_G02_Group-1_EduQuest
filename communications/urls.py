from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='communications_home'),
    path('addNewAnnouncement/', views.add_announcement, name='add_announcement'),
    path('index/', views.index, name='communications_index'),
]