"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mailings.urls", namespace="mailings")),
    path("users/", include("users.urls", namespace="users")),
    path("blog/", include("blogs.urls", namespace="blogs")),
]