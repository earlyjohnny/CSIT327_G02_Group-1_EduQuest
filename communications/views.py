from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Announcement

def announcements_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements.html', {'announcements': announcements})