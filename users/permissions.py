from rest_framework import permissions

from users.models import User

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser


class IsDebt(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_debt == False:
            return True

