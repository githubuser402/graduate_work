from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('menu/v1/', include('menu.urls')),
    path('public/v1/', include('public_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
