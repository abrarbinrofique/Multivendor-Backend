from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.profile, name="profile"),
    path("set_type", views.set_type, name="set_type"),
]
