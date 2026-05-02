from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Event, Venue


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    error = None

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid username or password. Please try again.'

    return render(request, 'events/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


def get_display_name(user):
    first = getattr(user, 'first_name', '') or ''
    last  = getattr(user, 'last_name',  '') or ''
    full  = f"{first} {last}".strip()
    if full:
        return full
    return (
        getattr(user, 'email', None) or
        getattr(user, 'username', None) or
        str(user)
    )


@login_required(login_url='login')
def home_view(request):
    return render(request, 'events/home.html', {
        'username': get_display_name(request.user),
    })


@login_required(login_url='login')
def edit_profile_view(request):
    saved = False
    user  = request.user

    if request.method == 'POST':
        first_name   = request.POST.get('first_name', '').strip()
        last_name    = request.POST.get('last_name',  '').strip()
        new_password = request.POST.get('new_password', '').strip()

        if hasattr(user, 'first_name'):
            user.first_name = first_name
        if hasattr(user, 'last_name'):
            user.last_name = last_name

        if new_password:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
        else:
            user.save()

        saved = True

    return render(request, 'events/edit_profile.html', {
        'username':   get_display_name(user),
        'first_name': getattr(user, 'first_name', '') or '',
        'last_name':  getattr(user, 'last_name',  '') or '',
        'saved':      saved,
    })


@login_required(login_url='login')
def add_record_view(request):
    saved = False
    error = None

    if request.method == 'POST':
        title       = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        date        = request.POST.get('date', '').strip()
        start_time  = request.POST.get('start_time', '').strip()
        end_time    = request.POST.get('end_time', '').strip()
        capacity    = request.POST.get('capacity', '').strip()
        venue_name  = request.POST.get('venue', '').strip()

        if title and description and date and start_time and end_time and capacity and venue_name:
            try:
                venue, _ = Venue.objects.get_or_create(
                    venue_name=venue_name,
                    defaults={
                        'building_location': 'TBD',  # ✅ max_occupancy removed
                    }
                )

                Event.objects.create(
                    title=title,
                    description=description,
                    date=date,
                    start_time=start_time,
                    end_time=end_time,
                    capacity=int(capacity),
                    venue=venue,
                    org=None,
                )
                saved = True

            except Exception as e:
                error = f'Could not save event: {e}'
        else:
            error = 'Please fill in all fields.'

    return render(request, 'events/add_record.html', {
        'username': get_display_name(request.user),
        'saved':    saved,
        'error':    error,
    })


@login_required(login_url='login')  # ✅ protected
def event_list(request):
    events = Event.objects.select_related('venue').order_by('date')
    return render(request, 'events/event_list.html', {
        'events':   events,
        'username': get_display_name(request.user),  # ✅ simplified, always logged in now
    })


@login_required(login_url='login')  # ✅ new venue view
def add_venue_view(request):
    from .forms import VenueForm
    error = None

    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = VenueForm()

    return render(request, 'events/addNewVenue.html', {
        'form':     form,
        'username': get_display_name(request.user),
    })