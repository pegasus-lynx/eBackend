from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "You don't have the permission to modify the reequested user profile."

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj

class IsUserAuthenticated(BasePermission):
    message = "You must be logged in to logout."

    def has_permission(self,request,view):
        return request.user.is_authenticated