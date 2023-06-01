from django.contrib import admin
from feeds.models  import FeedType, Feeds, FeedPics
from import_export.admin import ExportActionMixin, ImportExportModelAdmin

# Register your models here.

class FeedTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('type', 'type_desc', 'feed_unit', )
    list_filter = ('type', 'feed_unit')
    fieldsets = (
        (None, {'fields': ('type', 'type_desc')}),
        ('species info', {'fields': ('feed_unit',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type', 'feed_unit', 'type_desc', ),
        }),
    )
    search_fields = ('type', )
    ordering = ('type', )
    filter_horizontal = ()


class FeedsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cycle', 'feed_type', 'value', "time", 'lot', 'price_per_kg', 'is_probiotic_mixed','created_by', 'updated_by' )
    list_filter = ('cycle', 'feed_type', 'is_probiotic_mixed', 'value')
    fieldsets = (
        (None, {'fields': ('cycle', 'feed_type', 'value','time')}),
        ('species info', {'fields': ('lot', 'price_per_kg', 'is_probiotic_mixed', 'updated_by',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cycle', 'feed_type', 'value', ),
        }),
    )
    search_fields = ('cycle', )
    ordering = ('cycle', )
    filter_horizontal = ()



class FeedPicsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('image_name', 'image', 'images', "created_by", 'updated_by' )
    list_filter = ('image_name', 'created_by')
    fieldsets = (
        (None, {'fields': ('image_name', 'created_by', 'updated_by','images')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('image_name', 'created_by', 'images', ),
        }),
    )
    search_fields = ('image_name', )
    ordering = ('image_name', )
    filter_horizontal = ()





# Register your models here.
admin.site.register(FeedType, FeedTypeAdmin)
admin.site.register(Feeds, FeedsAdmin)
admin.site.register(FeedPics, FeedPicsAdmin)
