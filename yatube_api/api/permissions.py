from rest_framework import permissions, status
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response


class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
