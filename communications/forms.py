from django import forms
from .models import Announcement, Feedback, Document


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['headline', 'content']

        widgets = {
            'headline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter headline...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write announcement...'
            }),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comments']

        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rate from 1-5'
            }),
            'comments': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your feedback...'
            }),
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file_name', 'file']

        widgets = {
            'file_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter file name'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }