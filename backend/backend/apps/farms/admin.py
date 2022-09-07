from django.contrib import admin
from farms.models import Farms, FarmImage, FarmCertification


# Register your models here.

class FarmsAdmin(admin.ModelAdmin):
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('company_id', 'farm_name', 'farm_area', 'farm_status')
    list_filter = ('company_id',)
    fieldsets = (
        (None, {'fields': ('company_id', 'farm_name')}),
        ('Personal info', {'fields': (('farm_area', 'phone'), 'description','farm_status',  )}),
        ('Company info', {'fields': ('city', 'country', 'town_village', 'zipcode','state', )}),
        
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company_id', 'farm_area', 'farm_status', 'farm_name'),
        }),
    )
    search_fields = ('farm_name',)
    ordering = ('farm_name',)
    filter_horizontal = ()






admin.site.register(Farms,FarmsAdmin)
admin.site.register(FarmImage)
admin.site.register(FarmCertification)
