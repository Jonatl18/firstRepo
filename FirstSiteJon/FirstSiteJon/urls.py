from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("MyIndex/", include("MyIndex.urls")),
    path("admin/", admin.site.urls),
]