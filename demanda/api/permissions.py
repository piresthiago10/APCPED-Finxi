from rest_framework.permissions import BasePermission, SAFE_METHODS 


class IsOwnerOrReadOnly(BasePermission):
    """[apenas o dono pode editar seu próprio objeto]

    Args:
        BasePermission ([permission]): [ações para endpoints]
    """
    def has_object_permission(self, request, view, obj):

        print(obj.anunciante, request.user)
        return obj.anunciante == request.user
