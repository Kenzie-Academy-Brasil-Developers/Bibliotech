from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("obj:", obj)
        print("view:", view)
        print("request:", request)
        return request.user == obj.user or request.user.is_superuser
