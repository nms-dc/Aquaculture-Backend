from django.contrib import admin
from common.models import Country, Currency
from import_export.admin import ExportActionMixin


class CountryAdmin(ExportActionMixin, admin.ModelAdmin):

    list_display = ('alpha_2_code', 'alpha_3_code', 'country_name')
    list_filter = ('country_name', )
    fieldsets = (
        (None, {'fields': ('country_name', 'alpha_3_code')}),
        ('Company info', {'fields': ('alpha_2_code',)}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('country_name', 'alpha_2_code', 'alpha_3_code'),
        }),
    )
    search_fields = ('country_name',)
    ordering = ('country_name',)
    filter_horizontal = ()


class CurrencyAdmin(ExportActionMixin, admin.ModelAdmin):

    list_display = ('coutry_id', 'currency', 'fraction_number')
    list_filter = ('coutry_id', )
    fieldsets = (
        (None, {'fields': ('iso_code', 'fraction_unit')}),
        ('Company info', {'fields': ('symbol', 'currency', 'fraction_number')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('currency', 'coutry_id', 'fraction_unit'),
        }),
    )
    search_fields = ('currency',)
    ordering = ('currency',)
    filter_horizontal = ()


admin.site.register(Country, CountryAdmin)
admin.site.register(Currency, CurrencyAdmin)