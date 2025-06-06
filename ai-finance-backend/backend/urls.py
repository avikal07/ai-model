from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from django.http import HttpResponse  # type: ignore

# Simple homepage view
def home(request):
    return HttpResponse("<h1>Welcome to the AI Finance Assistant API</h1>")

urlpatterns = [
    path("", home),  # Root homepage
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")), 
]
