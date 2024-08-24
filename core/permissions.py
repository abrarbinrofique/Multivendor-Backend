from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsVendor(BasePermission):
    def has_permission(self, request, view):
        if not IsAuthenticated:
            return False
        return request.user.userprofile.type == "vendor"
    
    def has_object_permission(self, request, view, obj):
        return obj.vendor == request.user