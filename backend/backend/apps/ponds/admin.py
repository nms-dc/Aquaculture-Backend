from django.contrib import admin
from ponds.models import Ponds, PondType, PondConstructType, PondImage


class PondAdmin(admin.ModelAdmin):
    list_display = ('pond_name', 'pond_length', 'pond_depth', 'pond_breadth')
    list_filter = ('pond_name',)
    fieldsets = (
        (None, {'fields': ('pond_name', 'pond_length')}),
        ('Personal info', {'fields': ('pond_depth', 'pond_construct_type', 'lat', 'lng', 'is_active_pond', 'active_cycle_id')}),
        ('Company info', {'fields': ('pond_breadth', 'pond_area', 'pond_capacity', 'description', 'pond_number', 'current_stock_id')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('pond_name', 'pond_depth', 'pond_construct_type', 'pond_area'),
        }),
    )
    search_fields = ('pond_name',)
    ordering = ('pond_name',)
    filter_horizontal = ()


admin.site.register(PondType)
admin.site.register(PondConstructType)
admin.site.register(Ponds, PondAdmin)
admin.site.register(PondImage)
