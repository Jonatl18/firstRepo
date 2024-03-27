from django.urls import path

from . import views

urlpatterns = [
    path("", views.MyIndex, name="MyIndex"),
]