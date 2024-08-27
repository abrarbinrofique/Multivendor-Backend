from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

from product.models import Product, ProductImage

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsVendor(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.userprofile.type == "vendor"
    
    def has_object_permission(self, request, view, obj):
        if type(obj) is Product:
            return obj.vendor == request.user
        if type(obj) is ProductImage:
            return obj.product.vendor == request.user