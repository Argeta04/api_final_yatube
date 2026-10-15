from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Leitura para todos; alterar ou apagar só o autor do objeto."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)