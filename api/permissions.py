from rest_framework import permissions


class IsGoogleAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permission is only granted if user_info is not None
        return request.user_info is not None
