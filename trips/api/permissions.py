from rest_framework import permissions

class IsRider(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.account_type == 'rider'

class IsDriver(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.account_type == 'driver'

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.vehicle.owner == request.user