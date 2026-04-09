from django.views.generic.base import View
from django.shortcuts import render
from .models import Organization, Category


class HomeView(View):
    template_name = "organizations/index.html"

    def get(self, request):
        organizations = Organization.objects.all()
        categories = Category.objects.all()
        return render(request, self.template_name, {
            'organizations': organizations,
            'categories': categories,
        })
