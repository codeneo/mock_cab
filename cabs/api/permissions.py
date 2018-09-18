from rest_framework import permissions

class IsDriver(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.account_type == 'driver'

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user