from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Request, View

from users.models import User


class EmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, _: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user.is_authenticated and request.user.is_employee)


class AdminAndOwnerEdit(IsAuthenticated):
    def has_object_permission(self, request: Request, _: View, obj: User) -> bool:
        return request.user.is_employee or request.user == obj
