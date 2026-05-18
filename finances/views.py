from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import BudgetRequestForm, EditProfileForm


class FinancesLoginView(View):
	template_name = 'finances/login.html'

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('finances')
		return render(request, self.template_name)

	def post(self, request):
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('finances')
		else:
			messages.error(request, 'Invalid email or password.')
			return render(request, self.template_name)


class FinancesLogoutView(View):
	def get(self, request):
		logout(request)
		return redirect('finances_login')


class FinancesView(LoginRequiredMixin, View):
	template_name = 'finances/index.html'
	login_url = '/finances/login/'

	def get(self, request):
		return render(request, self.template_name)


class AddBudgetRequestView(LoginRequiredMixin, View):
	template_name = 'finances/addNewfinances.html'
	login_url = '/finances/login/'

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


class EditProfileView(LoginRequiredMixin, View):
	template_name = 'finances/edit_profile.html'
	login_url = '/finances/login/'

	def get(self, request):
		try:
			profile = request.user.profile
		except Exception:
			messages.error(request, 'No profile found for your account.')
			return redirect('finances')
		form = EditProfileForm(instance=profile)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		try:
			profile = request.user.profile
		except Exception:
			messages.error(request, 'No profile found for your account.')
			return redirect('finances')
		form = EditProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'Profile updated successfully.')
			return redirect('finances')
		return render(request, self.template_name, {'form': form})
