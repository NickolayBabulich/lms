from rest_framework.permissions import BasePermission


class IsNotModer(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return False
        return True


class IsNotModerForView(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            if view.action == 'create' or view.action == 'destroy':
                return False
        return True
