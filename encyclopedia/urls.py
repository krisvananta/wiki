from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/write/", views.add, name="write"),
    path("wiki/<str:title>/", views.entries, name="title"),
]
