from django.contrib import admin
from seeds.models import SeedImage, Seeds, SeedPlStage
from import_export.admin import ExportActionMixin, ImportExportModelAdmin

# Register your models here.

class SeedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('lot_number', 'number_of_eggs', 'date_sold', 'qr_code_id','quality')
    list_filter = ('lot_number', 'qr_code_id')
    fieldsets = (
        (None, {'fields': ('lot_number', 'date_sold')}),
        ('seed info', {'fields': ('number_of_eggs', 'date_received', 'date_hatched', "species", "species_pl_stage", "farm")}),
        ('moreinfoAboutSeed', {'fields': ('qr_code_id', 'quality', 'weight', 'price', 'seed_company_id')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('lot_number', 'number_of_eggs', 'qr_code_id', 'quality'),
        }),
    )
    search_fields = ('lot_number', )
    ordering = ('lot_number', )
    filter_horizontal = ()

    
class SeedImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('image', 'user', )
    list_filter = ('fish_ids', )
    fieldsets = (
        (None, {'fields': ('image', 'user', 'fish_ids')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('image', 'user', 'fish_ids', ),
        }),
    )
    search_fields = ('fish_ids',)
    ordering = ('fish_ids',)
    filter_horizontal = ()

class SeedPlStageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('type', 'type_description', )
    list_filter = ('type', )
    fieldsets = (
        (None, {'fields': ('type', 'type_description', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type_description', 'type', ),
        }),
    )
    search_fields = ('type',)
    ordering = ('type',)
    filter_horizontal = ()



admin.site.register(SeedImage, SeedImageAdmin)
admin.site.register(Seeds, SeedAdmin)
admin.site.register(SeedPlStage, SeedPlStageAdmin)