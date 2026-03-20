from django.contrib import admin
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('properties/', PropertyFilter.as_view() ),
    path('login', UserRegistrationsView.as_view() ),
    path('search-click/', UserClickSearchProperty.as_view() ),





]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)