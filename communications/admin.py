from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Announcement, Feedback, Document

admin.site.register(Announcement)
admin.site.register(Feedback)
admin.site.register(Document)