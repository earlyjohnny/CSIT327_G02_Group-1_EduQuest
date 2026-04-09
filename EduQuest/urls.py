from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # other modules
    path('accounts/', include('accounts.urls')),
    path('registrations/', include('registrations.urls')),
    path('organizations/', include('organizations.urls')),
    path('events/', include('events.urls')),

    # YOUR MODULE
    path('communications/', include('communications.urls')),
]

# for media files (documents)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)