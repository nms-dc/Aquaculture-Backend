from django.contrib import admin
from species.models import Species, SpeciesCategory

# Register your models here.

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_desc', 'image', )
    list_filter = ('fish_common_name', 'product_name')
    fieldsets = (
        (None, {'fields': ('product_name', 'product_desc')}),
        ('species info', {'fields': ('image', 'fish_common_name', 'fish_scientific_name', 'fish_ranges',)}),
        ('moreinfoAboutSeed', {'fields': ('wikipedia', 'createdAt', 'updatedAt',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('product_name', 'product_desc', 'fish_common_name', 'fish_ranges'),
        }),
    )
    search_fields = ('product_name', )
    ordering = ('product_name', )
    filter_horizontal = ()

    
class SpeciesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'exp', )
    list_filter = ('parent_category', )
    fieldsets = (
        (None, {'fields': ('slug', 'desc', 'image_url', 'species_category', 'name', 'exp', 'parent_category')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'species_category', 'desc', ),
        }),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
    
admin.site.register(SpeciesCategory, SpeciesCategoryAdmin)
admin.site.register(Species, SpeciesAdmin)
