from django.contrib import admin
from harvests.models import Harvests


class HarvestAdmin(admin.ModelAdmin):

    list_display = ('cycle', 'harvest_type', 'total_kgs', )
    list_filter = ('cycle', 'harvest_type')
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('harvest_type', 'harvest_cost')}),
        ('Harvest info', {'fields': (('total_kgs'), 'temperature', 'harvest_notes')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('harvest_type', 'harvest_cost', 'temperature', 'harvest_date'),
        }),
    )
    search_fields = ('harvest_type',)
    ordering = ('harvest_type',)
    filter_horizontal = ()


admin.site.register(Harvests, HarvestAdmin)
