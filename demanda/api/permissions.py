from rest_framework.permissions import BasePermission, SAFE_METHODS 


class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):

        print(obj.anunciante, request.user)
        return obj.anunciante == request.user