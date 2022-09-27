from django.contrib import admin
from harvests.models import Harvests


class HarvestAdmin(admin.ModelAdmin):

    list_display = ('harvest_type', 'harvest_cost', 'total_kgs', 'harvest_date')
    list_filter = ('harvest_type',)
    fieldsets = (
        (None, {'fields': ('harvest_type', 'harvest_cost')}),
        ('Personal info', {'fields': (('total_kgs'), 'temperature', 'harvest_animalImages', )}),
        ('Company info', {'fields': ('harvest_pondmages', 'harvest_logisticImages', 'harvest_notes', )}),
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
