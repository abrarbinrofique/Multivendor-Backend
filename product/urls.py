from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views


router = DefaultRouter()

router.register("list", views.ProductViewset, basename="list")

urlpatterns = router.urls + [
    path("create_order/", views.create_order, name="create_order"),
]
