from django.shortcuts import render, redirect
from .models import Announcement
from .forms import AnnouncementForm

def home(request):
    return render(request, 'communications/index.html')

def add_announcement(request):
    form = AnnouncementForm()

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('communications_home')

    return render(request, 'communications/addNewAnnouncement.html', {'form': form})