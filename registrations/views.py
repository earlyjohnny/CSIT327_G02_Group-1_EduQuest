from django.views import View
from django.shortcuts import render, redirect


class RegistrationsView(View):
    template_name = 'registrations_index.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, self.template_name)