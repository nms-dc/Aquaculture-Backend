from django.contrib import admin
from harvests.models import Harvests


class HarvestAdmin(admin.ModelAdmin):

    list_display = ('cycle', 'cycle', )
    list_filter = ('cycle',)
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('harvest_type', 'harvest_cost')}),
        ('Personal info', {'fields': (('total_kgs'), 'temperature',)}),
        ('Company info', {'fields': ('harvest_notes', )}),
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
