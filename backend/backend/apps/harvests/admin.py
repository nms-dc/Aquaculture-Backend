from django.contrib import admin
from harvests.models import Harvests, AddAnimal, HarvestAnimalImages,HarvestLogisticImages, HarvestPondImages
from import_export.admin import ExportActionMixin, ImportExportModelAdmin


class HarvestAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def farm_name(self, obj):
        return obj.cycle.Pond.farm
    
    def pond_name(self, obj):
        return obj.cycle.Pond
    

    list_display = ("farm_name","pond_name",'cycle', 'harvest_type', 'total_kgs', 'harvest_cost', "sold_to", "cycle", "animal_count_1",
     'temperature_celcius', 'harvest_notes','harvest_quality', "total_kg_1", "price_kg_1" )
    list_filter = ('cycle', 'harvest_type','cycle__Pond__farm__farm_name','cycle__Pond__pond_name')
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

    farm_name.admin_order_field = 'cycle__Pond__farm__farm_name' 
    pond_name.admin_order_field = 'cycle__Pond__pond_name'

    ordering = ('harvest_type',)
    filter_horizontal = ()


class AddAnimalAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def farm_name(self, obj):
        return obj.adding_animal.cycle.Pond.farm
    
    def pond_name(self, obj):
        return obj.adding_animal.cycle.Pond
    
    def harvest_name(self, obj):
        return obj.adding_animal

    list_display = ("farm_name","pond_name", 'harvest_name', 'animal_count', 'total_kg', )
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

    def farm_name(self, obj):
        return obj.images.cycle.Pond.farm
    
    def pond_name(self, obj):
        return obj.images.cycle.Pond
    
    def cycle_id(self, obj):
        return obj.images.cycle
   
    def harvest_name(self, obj):
        return obj.images
   

    list_display = ('farm_name','pond_name','cycle_id', 'harvest_name', 'image_name', 'image', 'images' )
    list_filter = ('image_name',)
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('image_name', 'image', 'images')}),
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

    def farm_name(self, obj):
        return obj.images.cycle.Pond.farm
    
    def pond_name(self, obj):
        return obj.images.cycle.Pond
    
    def cycle_id(self, obj):
        return obj.images.cycle
   
    def harvest_name(self, obj):
        return obj.images
   

    list_display = ('farm_name','pond_name','cycle_id','harvest_name','image_name', 'image', 'images' )
    list_filter = ('image_name',)
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('image_name', 'image', 'images')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('image_name', 'image', 'images'),
        }),
    )
    search_fields = ('image_name',)
    ordering = ('image_name',)
    filter_horizontal = ()


class LogisticImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def farm_name(self, obj):
        return obj.images.cycle.Pond.farm
    
    def pond_name(self, obj):
        return obj.images.cycle.Pond
    
    def cycle_id(self, obj):
        return obj.images.cycle
   
    def harvest_name(self, obj):
        return obj.images

    list_display = ('farm_name','pond_name','cycle_id','harvest_name','image_name', 'image', 'images')
    list_filter = ('image_name',)
    '''while trying to add fieldsets dont add the fields whih are all 'FK'    '''
    fieldsets = (
        (None, {'fields': ('image_name', 'image', 'images')}),
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
