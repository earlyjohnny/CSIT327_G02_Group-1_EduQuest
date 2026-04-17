from django import forms
from .models import Registration


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