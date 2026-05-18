from django import forms

from .models import BudgetRequest
from accounts.models import Profile


class BudgetRequestForm(forms.ModelForm):
	class Meta:
		model = BudgetRequest
		fields = ['org_id', 'doc_id', 'amount', 'purpose', 'status', 'request_date']
		widgets = {
			'request_date': forms.DateInput(attrs={'type': 'date'}),
		}


class EditProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'course', 'year_level']
		widgets = {
			'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
			'course': forms.TextInput(attrs={'placeholder': 'Course'}),
			'year_level': forms.TextInput(attrs={'placeholder': 'Year Level'}),
		}