from django import forms
from .models import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['cat', 'org_name', 'acronym', 'description', 'date_founded']
        labels = {
            'cat': 'Category',
            'org_name': 'Organization Name',
            'acronym': 'Acronym',
            'description': 'Description',
            'date_founded': 'Date Founded',
        }
        widgets = {
            'date_founded': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
