from django.contrib import admin
from .models import Company, CompanyFeedType
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
# Register your models here.


class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('company_name', 'address_one', 'address_two')
    list_filter = ('company_name', )
    fieldsets = (
        (None, {'fields': ('company_name', 'website')}),
        ('Company info', {'fields': ('pan_no', 'address_one', 'address_two', 'pincode',)}),
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


class CompanyFeedAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('type', 'type_description')
    list_filter = ('type',)
    fieldsets = (
        (None, {'fields': ('type', 'type_description')}),)
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type', 'type_description'),
        }),
    )
    search_fields = ('type',)
    ordering = ('type',)
    filter_horizontal = ()

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyFeedType, CompanyFeedAdmin)
