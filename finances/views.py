from django.views import View
from django.shortcuts import render

from .forms import BudgetRequestForm


class FinancesView(View):
	template_name = 'finances/index.html'

	def get(self, request):
		return render(request, self.template_name)


class AddBudgetRequestView(View):
	template_name = 'finances/addNewfinances.html'

	def get(self, request):
		form = BudgetRequestForm()
		return render(request, self.template_name, {'form': form, 'saved': False})

	def post(self, request):
		form = BudgetRequestForm(request.POST)
		if form.is_valid():
			form.save()
			return render(
				request,
				self.template_name,
				{'form': BudgetRequestForm(), 'saved': True}
			)
		return render(request, self.template_name, {'form': form, 'saved': False})
