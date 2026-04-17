from django.views import View
from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm


class RegistrationsView(View):
    template_name = 'index1.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        registrations = Registration.objects.all().order_by('-timestamp')
        return render(request, self.template_name, {'registrations': registrations})


class AddRegistrationView(View):
    template_name = 'addNewRegistration.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrations_index')

        return render(request, self.template_name, {'form': form})