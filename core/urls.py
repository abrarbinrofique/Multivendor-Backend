from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.profile, name="profile"),
    path("set_type", views.set_type, name="set_type"),
    path("set_shipping_address", views.set_shipping_address, name="set_shipping_address"),
]
