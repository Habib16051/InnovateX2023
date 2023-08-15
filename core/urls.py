from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls"), name="landing_page"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
