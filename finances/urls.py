from django.urls import path
from . import views

urlpatterns = [
    path('', views.FinancesView.as_view(), name='finances'),
    path('addNewBudgetRequest/', views.AddBudgetRequestView.as_view(), name='add_new_budget_request'),
]
