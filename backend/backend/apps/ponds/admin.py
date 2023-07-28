from django.contrib import admin
from ponds.models import Ponds, PondType, PondConstructType, PondImage, PondGraphs, PondAnalytics
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from mixins.control_mixins import PermissionClass


class PondAdmin(ImportExportModelAdmin, PermissionClass, admin.ModelAdmin):

    list_display = ('farm','pond_name', 'pond_length', 'pond_depth', 'pond_breadth','farm', 'pond_construct_type', 'lat', 
    'lng', 'is_active_pond', 'active_cycle_id', 'pond_breadth', 'pond_area', 'pond_capacity', 'description', 'pond_number')
    list_filter = ('farm', 'pond_name')
    fieldsets = (
        (None, {'fields': ('pond_name', 'pond_length')}),
        ('pond info', {'fields': ('pond_depth', 'pond_construct_type', 'lat', 'lng', 'is_active_pond', 'active_cycle_id',
                                      'active_cycle_date')}),
        ('moreinfoAboutPond', {'fields': ('pond_breadth', 'pond_area', 'pond_capacity', 'description', 'pond_number',
                                    )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('pond_name', 'pond_depth', 'pond_construct_type', 'pond_area'),
        }),
    )
    search_fields = ('pond_name', )
    ordering = ('pond_name', 'farm')
    filter_horizontal = ()


class PondAnalyticsAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def farm_name(self,obj):
        return obj.farm.farm_name
    
    def pond_name(self,obj):
        return obj.pond.pond_name

    list_display = ('farm_name', 'pond_name', 'harvest_amount','total_feed','extra_info')
    list_filter = ('pond', 'farm')
    fieldsets = (
        (None, {'fields': ('pond', 'farm','harvest_amount','total_feed','extra_info')}),
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


class PondGraphsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def farm_name(self,obj):
        return obj.farm.farm_name
    
    def pond_name(self,obj):
        return obj.pond.pond_name

    list_display = ('farm_name', 'pond_name','total_feed', 'abw', 'time')
    list_filter = ('farm', 'pond', )
    fieldsets = (
        (None, {'fields': ('pond', 'farm','total_feed', 'extra_info', 'abw')}),
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


class PondImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def farm_name(self,obj):
        return obj.images.farm
    
    def pond_name(self,obj):
        return obj.images.pond_name

    list_display = ('farm_name','pond_name','image', 'image_name',)
    list_filter = ('image_name',)
    fieldsets = (
        (None, {'fields': ('image_name', 'image', 'images')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('image_name', 'image_name', 'pond_name',),
        }),
    )
    search_fields = ('image_name',)
    ordering = ('image_name',)
    filter_horizontal = ()


class PondTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'desc',  'pond_construct')
    list_filter = ('pond_construct', 'name',)
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


class PondConstructTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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
