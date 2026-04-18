from django.views import View
from django.shortcuts import render, redirect


class FinancesView(View):
	template_name = 'finances/index.html'

	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('login')
		return render(request, self.template_name)
