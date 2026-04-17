from django import forms
from .models import Venue, Event

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venue_name', 'building_location']  # removed max_occupancy
        widgets = {
            'venue_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter venue name'
            }),
            'building_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter building location'
            }),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['org', 'venue', 'title', 'description', 'date', 'start_time', 'end_time', 'capacity']
        widgets = {
            'org': forms.Select(attrs={'class': 'form-select'}),
            'venue': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter capacity'}),
        }