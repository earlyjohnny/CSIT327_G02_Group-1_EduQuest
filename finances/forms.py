from django import forms

from .models import BudgetRequest


class BudgetRequestForm(forms.ModelForm):
	class Meta:
		model = BudgetRequest
		fields = ['org_id', 'doc_id', 'amount', 'purpose', 'status', 'request_date']
		widgets = {
			'request_date': forms.DateInput(attrs={'type': 'date'}),
		}