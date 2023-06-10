
#the request parameter what we are using will directly give the user who's aceesing records
class PermissionClass:
    def has_change_permission(self, request, obj=None):
        is_superuser = request.user.is_verified
        if is_superuser:
            return True
    
    def has_delete_permission(self, request, obj=None):
        
        is_superuser = request.user.is_verified
        if is_superuser:
            return True

    def has_add_permission(self, request, obj=None):
        
        is_superuser = request.user.is_verified
        if is_superuser:
            return True
