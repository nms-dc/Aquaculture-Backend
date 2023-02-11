from django.contrib import admin
from seeds.models import SeedImage, Seeds

# Register your models here.

class SeedAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'number_of_eggs', 'date_sold', 'qr_code_id','quality')
    list_filter = ('public_id', 'qr_code_id')
    fieldsets = (
        (None, {'fields': ('public_id', 'date_sold')}),
        ('seed info', {'fields': ('number_of_eggs', 'date_received', 'createdAt', 'updatedAt', 'date_hatched',)}),
        ('moreinfoAboutSeed', {'fields': ('qr_code_id', 'quality', 'weight', 'price', 'purchased_by_companyid',
                                     'seed_company_id')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('public_id', 'number_of_eggs', 'qr_code_id', 'quality'),
        }),
    )
    search_fields = ('public_id', )
    ordering = ('public_id', )
    filter_horizontal = ()

    
class SeedImageAdmin(admin.ModelAdmin):
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

admin.site.register(SeedImage, SeedImageAdmin)
admin.site.register(Seeds, SeedAdmin)