from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdminOrReadOnly(permissions.BasePermission):
     def has_permission(self, request, view):
         return   bool(request.method in SAFE_METHODS and request.user or request.user.is_staff)
        
