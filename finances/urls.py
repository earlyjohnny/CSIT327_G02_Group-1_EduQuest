from django.urls import path
from . import views

urlpatterns = [
    path('', views.FinancesView.as_view(), name='finances'),
]
