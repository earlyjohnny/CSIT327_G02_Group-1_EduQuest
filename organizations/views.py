from django.views.generic.base import View
from django.shortcuts import render, redirect
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


class LoginView(View):
    template_name = "index.html"

    def get(self, request):
        # If already logged in, skip login page
        if 'username' in request.session:
            return redirect('organizations:home_page')
        return render(request, self.template_name)

    def post(self, request):
        uname = request.POST['txt_username']
        pwd = request.POST['txt_password']
        try:
            user = User.objects.get(username=uname, password=pwd)
            request.session['username'] = uname
            request.session['user_type'] = user.type
            return redirect('organizations:home_page')
        except User.DoesNotExist:
            msg = 'Invalid credentials'
            return render(request, self.template_name, {'msg': msg})


class DashboardView(View):
    template_name = "home.html"

    def get(self, request):
        if 'username' not in request.session:
            return redirect('organizations:login')
        return render(request, self.template_name)


class EditProfileView(View):
    template_name = "edit_profile.html"

    def get(self, request):
        if 'username' not in request.session:
            return redirect('organizations:login')

        username = request.session.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            request.session.flush()
            return redirect('organizations:login')

        form = UserEditForm(instance=user)
        return render(request, self.template_name, {'form': form, 'username': username})

    def post(self, request):
        if 'username' not in request.session:
            return redirect('organizations:login')

        username = request.session.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            request.session.flush()
            return redirect('organizations:login')

        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)
            updated_user.password = form.cleaned_data['password']
            updated_user.save()
            return redirect('organizations:home_page')
        return render(request, self.template_name, {'form': form, 'username': username})


class AddCategoryView(View):
    template_name = "add_category.html"

    def get(self, request):
        if 'username' not in request.session:
            return redirect('organizations:login')
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if 'username' not in request.session:
            return redirect('organizations:login')

        success = None
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            success = 'Category added successfully!'
            form = CategoryForm()
        return render(request, self.template_name, {'form': form, 'success': success})


class LogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('organizations:login')


class RegisterView(View):
    template_name = "register.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        uname = request.POST['txt_username']
        pwd = request.POST['txt_password']
        confirm_pwd = request.POST['txt_confirm_password']

        if pwd != confirm_pwd:
            return render(request, self.template_name, {'msg': 'Passwords do not match'})

        if User.objects.filter(username=uname).exists():
            return render(request, self.template_name, {'msg': 'Username already taken'})

        User.objects.create(username=uname, password=pwd, type=1)
        return render(request, self.template_name, {'success': 'Account created successfully! You can now login.'})
