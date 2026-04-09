from django.shortcuts import render
from .models import Announcement, Feedback, Document

def communications_home(request):
    announcements = Announcement.objects.all()
    feedbacks = Feedback.objects.all()
    documents = Document.objects.all()

    return render(request, 'communications/home.html', {
        'announcements': announcements,
        'feedbacks': feedbacks,
        'documents': documents,
    })