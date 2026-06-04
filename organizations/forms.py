from django import forms
from .models import Organization, User, Category


class OrganizationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Select a category"

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


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
        labels = {
            'username': 'Username',
            'password': 'Password',
            'first_name': 'Firstname',
            'last_name': 'Lastname',
        }
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']
        labels = {
            'category_name': 'Category Name',
            'description': 'Description',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
