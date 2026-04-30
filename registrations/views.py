from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash
from .models import Registration, Attendance
from .forms import RegistrationForm, AttendanceForm, EditProfileForm


class RegistrationsHomeView(View):
    template_name = 'home.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, self.template_name)


class RegistrationsIndexView(View):
    template_name = 'index1.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        registrations = Registration.objects.all()
        return render(request, self.template_name, {'registrations': registrations})


class AttendanceIndexView(View):
    template_name = 'index2.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        attendances = Attendance.objects.all()
        return render(request, self.template_name, {'attendances': attendances})


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


class AddAttendanceView(View):
    template_name = 'addNewAttendance.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = AttendanceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_index')
        return render(request, self.template_name, {'form': form})


class EditProfileView(View):
    template_name = 'editprofile.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = EditProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('registrations_home')
        return render(request, self.template_name, {'form': form})


class RegistrationsLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')