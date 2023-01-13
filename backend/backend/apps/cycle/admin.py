from django.contrib import admin
from cycle.models import Cycle, CycleAnalytics
from django.contrib.auth.models import Group


class CycleAdmin(admin.ModelAdmin):

    '''The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.'''
    list_display = ('Pond','species', 'species_pl_stage', 'invest_amount', 'seeding_date')
    list_filter = ('Pond',)
    fieldsets = (
        (None, {'fields': ('species', 'species_pl_stage')}),
        ('Personal info', {'fields': ('invest_amount', 'pondPrep_cost', 'description', )}),
        ('Company info', {'fields': ('seed_company', 'Pond')}),
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

    '''The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.'''
    list_display = ('farm', 'pond', 'cycle',)
    list_filter = ('farm',)
    fieldsets = (
        (None, {'fields': ('farm', 'pond')}),
        ('Personal info', {'fields': ('cycle', 'harvest_amount', )}),
        ('Company info', {'fields': ('total_feed', 'extra_info',)}),
       )
    ''' add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.'''
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('farm', 'pond', 'cycle', 'harvest_amount'),
        }),
    )
    search_fields = ('cycle', )
    ordering = ('cycle', )
    filter_horizontal = ()


admin.site.register(Cycle, CycleAdmin)
admin.site.register(CycleAnalytics, CycleAnalyticsAdmin)
