from django.contrib import admin
from cycle.models import Cycle, CycleAnalytics
from django.contrib.auth.models import Group
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from mixins.control_mixins import PermissionClass


class CycleAdmin(ImportExportModelAdmin, PermissionClass, admin.ModelAdmin):
    
    def farm_name(self, obj):
        return obj.Pond.farm

    '''The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.'''
    list_display = ('farm_name','Pond', 'seeds', 'numbers_of_larva', 'seeding_qty', 'species_weight', 'harvest_id')
    list_filter = ('Pond', 'seeds','Pond__farm__farm_name')
    fieldsets = (
        (None, {'fields': ( 'Pond', "seeding_qty", "seeding_date", "harvest_id", "seed_transfer_date", 'seeds')}),
        ('Cycle info', {'fields': ( 'pondPrep_cost', 'description', 'numbers_of_larva', 'is_active', "species_weight")})
        )
    ''' add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.'''
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("description", "seeding_qty", "numbers_of_larva", 'pondPrep_cost', ),
        }),
    )
    search_fields = ('seeds',)
    farm_name.admin_order_field = 'Pond__farm__farm_name'  # Allow sorting on this field
    ordering = ('Pond', 'seeds',)
    filter_horizontal = ()


class CycleAnalyticsAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    '''The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.'''
    list_display = ('farm', 'pond', 'cycle','harvest_amount', 'total_feed', 'total_probiotics')
    list_filter = ('farm', 'pond')
    fieldsets = (
        (None, {'fields': ('farm', 'pond')}),
        ('Analytics info', {'fields': ('cycle', 'harvest_amount', 'total_feed', 'total_probiotics','extra_info',)})        
       )
    ''' add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.'''
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('farm', 'pond', 'cycle', 'harvest_amount','total_feed','total_probiotics'),
        }),
    )
    search_fields = ('cycle', )
    ordering = ('cycle', 'farm', 'pond')
    filter_horizontal = ()


admin.site.register(Cycle, CycleAdmin)
admin.site.register(CycleAnalytics, CycleAnalyticsAdmin)
