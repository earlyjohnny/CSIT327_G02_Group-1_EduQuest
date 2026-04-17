from django.shortcuts import render, redirect
from .forms import EventForm, VenueForm
from .models import Event, Venue

def index(request):
    events = Event.objects.all()  # fetch all events
    return render(request, 'events/index.html', {'events': events})

def add_new_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:index')
    else:
        form = EventForm()
    return render(request, 'events/addNewEvent.html', {'form': form})

def add_new_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:index')
    else:
        form = VenueForm()
    return render(request, 'events/addNewVenue.html', {'form': form})