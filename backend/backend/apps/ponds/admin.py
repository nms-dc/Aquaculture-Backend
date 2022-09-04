from django.contrib import admin
from ponds.models import Ponds, PondType, PondConstructType, PondImage
# Register your models here.

class PondAdmin(admin.ModelAdmin):
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('pond_name', 'pond_length', 'pond_depth', 'pond_breadth')
    list_filter = ('pond_name',)
    fieldsets = (
        (None, {'fields': ('pond_name', 'pond_length')}),
        ('Personal info', {'fields': ( 'pond_depth','pond_construct_type','lat','lng',  )}),
        ('Company info', {'fields': ('pond_breadth', 'pond_area', 'pond_capacity','description','pond_number','current_stock_id' )}),
        
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('pond_name', 'pond_depth', 'pond_construct_type', 'pond_area'),
        }),
    )
    search_fields = ('pond_name',)
    ordering = ('pond_name',)
    filter_horizontal = ()






admin.site.register(PondType)
admin.site.register(PondConstructType)
admin.site.register(Ponds, PondAdmin)
admin.site.register(PondImage)
