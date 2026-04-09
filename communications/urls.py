from django.urls import path
from .views import announcements_list

urlpatterns = [
    path('', announcements_list, name='announcements'),
]