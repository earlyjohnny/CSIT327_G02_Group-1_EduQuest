from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from .models import Announcement, Feedback, Document
from .forms import AnnouncementForm, FeedbackForm, DocumentForm


def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('communications_home')
    return redirect('communications_login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('communications_home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('communications_home')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'communications/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('communications_home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'communications/register.html')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'communications/register.html')

        user_model = get_user_model()
        if user_model.objects.filter(email=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'communications/register.html')

        user = user_model.objects.create_user(email=username, password=password)
        login(request, user)
        return redirect('communications_home')

    return render(request, 'communications/register.html')


def logout_view(request):
    logout(request)
    return redirect('communications_login')


@login_required(login_url='communications_login')
def home(request):
    announcements = Announcement.objects.all().order_by('-date_posted')
    feedbacks = Feedback.objects.all().order_by('-submission_date')
    documents = Document.objects.all().order_by('-upload_date')

    return render(request, 'communications/home.html', {
        'announcements': announcements,
        'feedbacks': feedbacks,
        'documents': documents,
    })


@login_required(login_url='communications_login')
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

@login_required(login_url='communications_login')
def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('communications_home')

    else:
        form = FeedbackForm()

    return render(
        request,
        'communications/addFeedback.html',
        {'form': form}
    )


@login_required(login_url='communications_login')
def add_document(request):
    if request.method == 'POST':
        form = DocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('communications_home')

    else:
        form = DocumentForm()

    return render(
        request,
        'communications/addDocument.html',
        {'form': form}
    )


@login_required(login_url='communications_login')
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        student_num = request.POST.get('student_num', '').strip()
        course = request.POST.get('course', '').strip()
        year_level = request.POST.get('year_level', '').strip()

        if not email:
            messages.error(request, 'Email is required.')
        elif not student_num:
            messages.error(request, 'Student number is required.')
        elif not first_name or not last_name:
            messages.error(request, 'First name and last name are required.')
        else:
            user_model = get_user_model()
            if user_model.objects.exclude(pk=request.user.pk).filter(email=email).exists():
                messages.error(request, 'Email is already in use.')
            else:
                request.user.email = email
                request.user.save(update_fields=['email'])

                if profile is None:
                    profile = Profile(
                        user=request.user,
                        student_num=student_num,
                    )
                elif profile.student_num != student_num:
                    if Profile.objects.exclude(user=request.user).filter(student_num=student_num).exists():
                        messages.error(request, 'Student number is already in use.')
                        return render(request, 'communications/editProfile.html', {'profile': profile})
                    profile.student_num = student_num

                profile.first_name = first_name
                profile.last_name = last_name
                profile.course = course
                profile.year_level = year_level
                profile.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('communications_edit_profile')

    return render(request, 'communications/editProfile.html', {'profile': profile})


def index(request):
    return redirect('communications_login')