from django.shortcuts import render, redirect
from .models import Announcement, Feedback, Document
from .forms import AnnouncementForm


# 📌 COMMUNICATIONS HOME (cards UI)
def home(request):
    announcements = Announcement.objects.all().order_by('-date_posted')
    feedbacks = Feedback.objects.all().order_by('-submission_date')
    documents = Document.objects.all().order_by('-upload_date')

    return render(request, 'communications/home.html', {
        'announcements': announcements,
        'feedbacks': feedbacks,
        'documents': documents,
    })


# 📌 ADD NEW ANNOUNCEMENT
def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('communications_home')
    else:
        form = AnnouncementForm()

    return render(request, 'communications/addNewAnnouncement.html', {
        'form': form
    })


# 📌 OPTIONAL: SIMPLE INDEX (for your activity requirement)
def index(request):
    return render(request, 'communications/index.html')