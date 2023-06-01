from django.contrib import admin
from harvests.models import Harvests, AddAnimal, HarvestAnimalImages,HarvestLogisticImages, HarvestPondImages
from import_export.admin import ExportActionMixin, ImportExportModelAdmin


class HarvestAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def farm_name(self, obj):
        return obj.cycle.Pond.farm.farm_name
    
    def pond_name(self, obj):
        return obj.cycle.Pond.pond_name
    

    list_display = ("farm_name","pond_name",'cycle', 'harvest_type', 'total_kgs', 'harvest_cost', "sold_to", "cycle", "animal_count_1",
     'temperature_celcius', 'harvest_notes','harvest_quality', "total_kg_1", "price_kg_1" )
    list_filter = ('cycle', 'harvest_type')
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('harvest_type', 'harvest_cost', "sold_to", "cycle", "animal_count_1")}),
        ('Harvest info', {'fields': (('total_kgs'), 'temperature_celcius', 'harvest_notes','harvest_quality', "total_kg_1", "price_kg_1")}),
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


class AddAnimalAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def farm_name(self, obj):
        return obj.adding_animal.cycle.Pond.farm.farm_name
    
    def pond_name(self, obj):
        return obj.adding_animal.cycle.Pond.pond_name
    

    list_display = ("farm_name","pond_name", 'animal_count', 'total_kg', )
    list_filter = ('animal_count', 'total_kg', 'adding_animal')
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('animal_count', 'total_kg', "price_kg", "adding_animal")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('animal_count', 'total_kg', 'price_kg', 'adding_animal'),
        }),
    )
    search_fields = ('animal_count',)
    ordering = ('animal_count',)
    filter_horizontal = ()


class AnimalImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    # def farm_name(self, obj):
    #     return obj.images.cycle.farm
    
    # def pond_name(self, obj):
    #     return obj.images.cycle.Pond.pond_name
    

    list_display = ( 'image_name', 'image', )
    list_filter = ('image_name',)
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('image_name', 'image')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('image_name', 'image'),
        }),
    )
    search_fields = ('image_name',)
    ordering = ('image_name',)
    filter_horizontal = ()


class PondImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    # def farm_name(self, obj):
    #     return obj.images.cycle.Pond.farm.farm_name
    
    # def pond_name(self, obj):
    #     return obj.images.cycle.Pond.pond_name
    

    list_display = ('image_name', 'image', )
    list_filter = ('image_name',)
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('image_name', 'image')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('image_name', 'image'),
        }),
    )
    search_fields = ('image_name',)
    ordering = ('image_name',)
    filter_horizontal = ()


class LogisticImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    # def farm_name(self, obj):
    #     return obj.images.cycle.Pond.farm.farm_name
    
    # def pond_name(self, obj):
    #     return obj.images.cycle.Pond.pond_name
    

    list_display = ('image_name', 'image', )
    list_filter = ('image_name',)
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('image_name', 'image')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('image_name', 'image'),
        }),
    )
    search_fields = ('image_name',)
    ordering = ('image_name',)
    filter_horizontal = ()



admin.site.register(Harvests, HarvestAdmin)
admin.site.register(AddAnimal, AddAnimalAdmin)
admin.site.register(HarvestAnimalImages, AnimalImagesAdmin)
admin.site.register(HarvestPondImages, PondImagesAdmin)
admin.site.register(HarvestLogisticImages, LogisticImagesAdmin)
