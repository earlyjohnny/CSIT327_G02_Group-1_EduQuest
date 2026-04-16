from django.views.generic.base import View
from django.shortcuts import render, redirect
from .models import Organization, Category
from .forms import OrganizationForm


class HomeView(View):
    template_name = "organizations/index.html"

    def get(self, request):
        organizations = Organization.objects.all()
        categories = Category.objects.all()
        return render(request, self.template_name, {
            'organizations': organizations,
            'categories': categories,
        })


class AddOrganizationView(View):
    template_name = "organizations/addNewOrganization.html"

    def get(self, request):
        form = OrganizationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizations:index')
        return render(request, self.template_name, {'form': form})
