from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name = "home"),
    path("user", views.user, name = "user"),
    path("user/<login>", views.user, name = "user"),
    path("user/<login>/<str:folder>", views.user, name = "user"),
    path("user/<login>/<str:folder>/<int:post>", views.user, name = "user"),
    path("error", views.error, name = "error")
]