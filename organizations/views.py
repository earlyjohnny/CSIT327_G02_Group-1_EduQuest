from django.views.generic.base import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Organization, Category, User
from .forms import OrganizationForm, UserEditForm, CategoryForm


class HomeView(View):
    template_name = "organizations/index.html"

    def get(self, request):
        organizations = Organization.objects.all()
        categories = Category.objects.all()
        return render(request, self.template_name, {
            'organizations': organizations,
            'categories': categories,
        })


class AddOrganizationView(View):
    template_name = "organizations/addNewOrganization.html"

    def get(self, request):
        form = OrganizationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizations:index')
        return render(request, self.template_name, {'form': form})


# LOGIN / INDEX VIEW
def home(request):
    # If already logged in, skip login page
    if 'username' in request.session:
        return redirect('organizations:home_page')

    if request.method == 'POST':
        uname = request.POST['txt_username']
        pwd = request.POST['txt_password']
        try:
            user = User.objects.get(username=uname, password=pwd)
            request.session['username'] = uname
            request.session['user_type'] = user.type
            return redirect('organizations:home_page')
        except User.DoesNotExist:
            msg = 'Invalid credentials'
            return render(request, 'index.html', {'msg': msg})

    return render(request, 'index.html')


# HOME PAGE VIEW
def home_page(request):
    if 'username' not in request.session:
        return redirect('organizations:login')
    return render(request, 'home.html')


# EDIT PROFILE VIEW
def edit_profile(request):
    if 'username' not in request.session:
        return redirect('organizations:login')

    username = request.session.get('username')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        request.session.flush()
        return redirect('organizations:login')

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)
            updated_user.password = form.cleaned_data['password']
            updated_user.save()
            return redirect('organizations:home_page')
    else:
        form = UserEditForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form, 'username': username})


# ADD NEW RECORD VIEW
def add_record(request):
    if 'username' not in request.session:
        return redirect('organizations:login')

    success = None
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            success = 'Organization added successfully!'
            form = OrganizationForm()
    else:
        form = OrganizationForm()

    return render(request, 'add_record.html', {'form': form, 'success': success})


# ADD CATEGORY VIEW
def add_category(request):
    if 'username' not in request.session:
        return redirect('organizations:login')

    success = None
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            success = 'Category added successfully!'
            form = CategoryForm()
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form, 'success': success})


# LOGOFF VIEW
def logoff(request):
    request.session.flush()
    return redirect('organizations:login')


# REGISTER VIEW
def register(request):
    if request.method == 'POST':
        uname = request.POST['txt_username']
        pwd = request.POST['txt_password']
        confirm_pwd = request.POST['txt_confirm_password']
        user_type = request.POST['txt_type']

        if pwd != confirm_pwd:
            return render(request, 'register.html', {'msg': 'Passwords do not match'})

        if User.objects.filter(username=uname).exists():
            return render(request, 'register.html', {'msg': 'Username already taken'})

        User.objects.create(username=uname, password=pwd, type=int(user_type))
        return render(request, 'register.html', {'success': 'Account created successfully! You can now login.'})

    return render(request, 'register.html')
