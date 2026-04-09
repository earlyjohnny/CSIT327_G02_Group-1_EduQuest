from django.urls import path
from .views import communications_home

urlpatterns = [
    path('', communications_home, name='communications_home'),
]