from django.contrib import admin
from cycle.models import Cycle, CycleAnalytics
from django.contrib.auth.models import Group


class CycleAdmin(admin.ModelAdmin):
    
    def farm_name(self, obj):
        return obj.Pond.farm.farm_name
    
    def pond_name(self, obj):
        return obj.Pond.pond_name
    
    def cycle_name(self, obj):
        return f"cycle_id:{obj.id}"

    '''The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.'''
    list_display = ('farm_name','pond_name',"cycle_name",'species', 'species_pl_stage', 'invest_amount', 'seeding_date')
    list_filter = ('Pond', 'species')
    fieldsets = (
        (None, {'fields': ('species', 'species_pl_stage')}),
        ('Cycle info', {'fields': ('invest_amount', 'pondPrep_cost', 'description', 'seed_company', 'Pond', 'numbers_of_larva', 'is_active')})
        )
    ''' add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.'''
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('species', 'species_pl_stage', 'pondPrep_cost', 'invest_amount'),
        }),
    )
    search_fields = ('species',)
    ordering = ('species',)
    filter_horizontal = ()


class CycleAnalyticsAdmin(admin.ModelAdmin):

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
