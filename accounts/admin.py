from django.contrib import admin
from .models import User, Profile, Role, Membership

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Membership)