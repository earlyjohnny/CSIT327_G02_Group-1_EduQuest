from django.urls import path
from . import views

urlpatterns = [
    path('', views.FinancesView.as_view(), name='finances'),
    path('login/', views.FinancesLoginView.as_view(), name='finances_login'),
    path('logout/', views.FinancesLogoutView.as_view(), name='finances_logout'),
    path('addNewBudgetRequest/', views.AddBudgetRequestView.as_view(), name='add_new_budget_request'),
    path('profile/edit/', views.EditProfileView.as_view(), name='finances_edit_profile'),
]
