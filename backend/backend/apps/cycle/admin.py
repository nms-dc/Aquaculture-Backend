from django.contrib import admin
from cycle.models import Cycle
from django.contrib.auth.models import Group


# Register your models here.
class CycleAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('species', 'species_pl_stage', 'invest_amount', 'seeding_date')
    list_filter = ('species',)
    fieldsets = (
        (None, {'fields': ('species', 'species_pl_stage')}),
        ('Personal info', {'fields': ('invest_amount', 'pondPrep_cost', 'description', )}),
        ('Company info', {'fields': ('seed_company', )}),
       )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('species', 'species_pl_stage', 'pondPrep_cost', 'invest_amount'),
        }),
    )
    search_fields = ('species',)
    ordering = ('species',)
    filter_horizontal = ()


admin.site.register(Cycle, CycleAdmin)
