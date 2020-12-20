"""from rest_framework import permissions  

class IsShopUser(permissions.BasePermission):
    """
    #Permission is User the same as the requested User
    """

    def has_permission(self, request, view):
        user_id = request.user
        print(view)
"""