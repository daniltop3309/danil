from django.urls import path, include
from main import views



urlpatterns = [
    path('', include("main.urls"), name = "home"),
]
