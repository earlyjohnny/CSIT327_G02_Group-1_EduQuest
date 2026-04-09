from django.shortcuts import render
from datetime import date, time


def event_list(request):
    # Dummy events data
    events = [
        {
            'title': 'Science Fair',
            'description': 'A fun day of science exhibits.',
            'date': date(2026, 4, 15),
            'start_time': time(9, 0),
            'end_time': time(12, 0),
            'venue': 'Main Hall',
            'capacity': 100
        },
        {
            'title': 'Art Workshop',
            'description': 'Learn to paint like a pro.',
            'date': date(2026, 4, 20),
            'start_time': time(14, 0),
            'end_time': time(16, 0),
            'venue': 'Art Room',
            'capacity': 30
        }
    ]

    context = {'events': events}
    return render(request, 'events/event_list.html', context)