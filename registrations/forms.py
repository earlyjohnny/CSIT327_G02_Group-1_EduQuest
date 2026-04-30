from django import forms
from .models import Registration, Attendance
from accounts.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['user', 'event', 'confirmation_code']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
            'confirmation_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. EQ-2026-ABC'
            }),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['user', 'event', 'org', 'time_in', 'time_out', 'is_excused']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
            'org': forms.Select(attrs={'class': 'form-control'}),
            'time_in': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'time_out': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'is_excused': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class EditProfileForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Leave blank to keep current password'}),
        label='Password'
    )

    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user