from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('communications.urls')),
    path('accounts/', include('accounts.urls')),
    path('registrations/', include('registrations.urls')),
    path('organizations/', include('organizations.urls')),
    path('events/', include('events.urls')),
    path('finances/', include('finances.urls')),
    path('communications/', include('communications.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)