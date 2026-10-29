from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("users/", include("user.urls", namespace="user")),
    path("__debug__/", include("debug_toolbar.urls")),
]
