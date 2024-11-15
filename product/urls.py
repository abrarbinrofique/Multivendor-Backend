from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views


router = DefaultRouter()

router.register("list", views.ProductViewset, basename="list")
router.register("images", views.ProductImageViewset, basename="images")
router.register("orderitem", views.Orderitemviewset, basename="orderitem")
router.register("order", views.Orderviewset, basename="order")

urlpatterns = router.urls + [
    path("create_order/", views.create_order, name="create_order"),
]
