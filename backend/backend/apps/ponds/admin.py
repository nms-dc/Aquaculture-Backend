from django.contrib import admin
from ponds.models import Ponds, PondType, PondConstructType, PondImage, PondGraphs, PondAnalytics


class PondAdmin(admin.ModelAdmin):
    list_display = ('pond_name', 'pond_length', 'pond_depth', 'pond_breadth','farm')
    list_filter = ('farm',)
    fieldsets = (
        (None, {'fields': ('pond_name', 'pond_length')}),
        ('Personal info', {'fields': ('pond_depth', 'pond_construct_type', 'lat', 'lng', 'is_active_pond', 'active_cycle_id',
                                      'active_cycle_date')}),
        ('Company info', {'fields': ('pond_breadth', 'pond_area', 'pond_capacity', 'description', 'pond_number',
                                     'current_stock_id')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('pond_name', 'pond_depth', 'pond_construct_type', 'pond_area'),
        }),
    )
    search_fields = ('pond_name', )
    ordering = ('pond_name', )
    filter_horizontal = ()


class PondAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('farm', 'pond', 'no_of_cycles')
    list_filter = ('pond',)
    fieldsets = (
        (None, {'fields': ('pond', 'farm','no_of_cycles','harvest_amount','total_feed','extra_info')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('total_feed', 'harvest_amount', 'farm', 'extra_info'),
        }),
    )
    search_fields = ('pond', )
    ordering = ('pond', )
    filter_horizontal = ()


class PondGraphsAdmin(admin.ModelAdmin):
    list_display = ('farm', 'pond', 'time','total_feed', 'abw')
    list_filter = ('pond', )
    fieldsets = (
        (None, {'fields': ('pond', 'farm')}),
        ('Personal info', {'fields': ( 'abw', )}),
        ('Company info', {'fields': ('total_feed', 'extra_info', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('total_feed', 'harvest_amount', 'time', 'extra_info'),
        }),
    )
    search_fields = ('pond',)
    ordering = ('pond',)
    filter_horizontal = ()


class PondImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'image_name',)
    list_filter = ('image_name',)
    fieldsets = (
        (None, {'fields': ('image_name', 'image')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('image_name', 'image_name', 'images',),
        }),
    )
    search_fields = ('image_name',)
    ordering = ('image_name',)
    filter_horizontal = ()


class PondTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc',)
    list_filter = ('pond_construct',)
    fieldsets = (
        (None, {'fields': ('name', 'desc')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'desc', 'pond_construct',),
        }),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


class PondConstructTypeAdmin(admin.ModelAdmin):
    list_display = ('construct_type', )
    list_filter = ('construct_type',)
    fieldsets = (
        (None, {'fields': ('construct_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('construct_type',),
        }),
    )
    search_fields = ('construct_type',)
    ordering = ('construct_type',)
    filter_horizontal = ()


admin.site.register(PondType, PondTypeAdmin)
admin.site.register(PondConstructType, PondConstructTypeAdmin)
admin.site.register(Ponds, PondAdmin)
admin.site.register(PondImage, PondImageAdmin)
admin.site.register(PondGraphs, PondGraphsAdmin)
admin.site.register(PondAnalytics, PondAnalyticsAdmin)
