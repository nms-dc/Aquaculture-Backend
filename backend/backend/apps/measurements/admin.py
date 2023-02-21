from django.contrib import admin
from measurements.models import Measurement, MeasurementMaster, MeasurementPics


class MeasurementAdmin(admin.ModelAdmin):
    def farm_name(self, obj):
        return obj.cycle.Pond.farm.farm_name
    
    def pond_name(self, obj):
        return obj.cycle.Pond.pond_name

    list_display = ('farm_name','pond_name', 'measurement_type','cycle', 'value', 'time', 'lot')
    list_filter = ('cycle', )
    fieldsets = (
        (None, {'fields': ('cycle', 'value')}),
        ('Measurement info', {'fields': (('time', 'lot'), 'price_per_kg', 'measurement_type', 'is_probiotic_mixed')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('measurement_type', 'value', 'lot'),
        }),
    )
    search_fields = ('cycle',)
    ordering = ('measurement_type',)


class MeasurementmasterAdmin(admin.ModelAdmin):

    list_display = ('measurement_type', 'measurement_description' )
    list_filter = ('measurement_type', )
    fieldsets = (
        (None, {'fields': ('measurement_type', 'measurement_description', 'measurement_logo')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('measurement_type', ),
        }),
    )
    search_fields = ('measurement_description',)
    ordering = ('measurement_type',)

    filter_horizontal = ()


admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(MeasurementMaster, MeasurementmasterAdmin)
admin.site.register(MeasurementPics)