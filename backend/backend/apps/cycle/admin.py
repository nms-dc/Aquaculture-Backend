from django.contrib import admin
from cycle.models import Cycle, CycleAnalytics
from django.contrib.auth.models import Group
from import_export.admin import ExportActionMixin, ImportExportModelAdmin


class CycleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    def farm_name(self, obj):
        return obj.Pond.farm.farm_name
    
    def pond_name(self, obj):
        return obj.Pond.pond_name
    
    def seeds_name(self, obj):
        return obj.seeds.lot_number    
    
    '''The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.'''
    list_display = ('farm_name','pond_name', 'seeds_name')
    list_filter = ('Pond', )
    fieldsets = (
        (None, {'fields': ( 'Pond', "seeding_qty", "seeding_date", "harvest_id", "seed_transfer_date")}),
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
    ordering = ('seeds',)
    filter_horizontal = ()


class CycleAnalyticsAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def farm_name(self, obj):
        return obj.farm.farm_name
    
    def pond_name(self, obj):
        return obj.pond.pond_name


    '''The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.'''
    list_display = ('farm_name', 'pond_name', 'cycle','harvest_amount', 'total_feed', 'total_probiotics')
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
    ordering = ('cycle', )
    filter_horizontal = ()


admin.site.register(Cycle, CycleAdmin)
admin.site.register(CycleAnalytics, CycleAnalyticsAdmin)
