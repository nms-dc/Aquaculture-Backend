from django.contrib import admin
from .models import Company, CompanyFeedType
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('company_name', 'address_one', 'address_two')
    list_filter = ('company_name', 'address_one')
    fieldsets = (
        (None, {'fields': ('company_name', 'website')}),
        ('Company info', {'fields': ('pan_no', 'address_one', 'address_two', 'pincode', 'company_type')}),
        )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company_name', 'address_one', 'address_two', 'pincode'),
        }),
    )
    search_fields = ('company_name',)
    ordering = ('company_name',)
    filter_horizontal = ()


class CompanyFeedAdmin(admin.ModelAdmin):

    list_display = ('company', 'feed_type')
    list_filter = ('company',)
    fieldsets = (
        (None, {'fields': ('company', 'feed_type')}),)
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company', 'feed_type'),
        }),
    )
    search_fields = ('company',)
    ordering = ('company',)
    filter_horizontal = ()

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyFeedType, CompanyFeedAdmin)
