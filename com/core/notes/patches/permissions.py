# permissions.py
from rest_framework import permissions

class IsAdminOrObjectOwner(permissions.BasePermission):
    """ Allow object editing only staff or object owner
    """
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method not in permissions.SAFE_METHODS:
            if request.user.is_staff:
                return True

            if hasattr(obj, 'user'):
                return obj.user == request.user

            if hasattr(obj, 'author'):
                return obj.author.user == request.user

            if hasattr(obj, 'username'):
                return obj.username == request.user.username

            else:
                return False
