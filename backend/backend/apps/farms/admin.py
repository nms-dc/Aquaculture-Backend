from django.contrib import admin
from farms.models import Farms, FarmImage, FarmCertification, FeedLots, FarmAnalytics


# Register your models here.

class FarmsAdmin(admin.ModelAdmin):

    list_display = ('farm_name', 'farm_area', 'farm_status', 'company_id')
    list_filter = ('company_id', 'farm_name', )
    fieldsets = (
        (None, {'fields': ('company_id', 'farm_name')}),
        ('Farm info', {'fields': (('farm_area', 'phone'), 'description', 'farm_status', )}),
        ('Address info', {'fields': ('city', 'country', 'town_village', 'zipcode', 'state', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company_id', 'farm_area', 'farm_status', 'farm_name'),
        }),
    )
    search_fields = ('farm_name',)
    ordering = ('farm_name',)
    filter_horizontal = ()




class FarmAnalyticsAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    def farm_name(self,obj):
        return obj.farm.farm_name
    
    list_display = ('farm_name', 'no_of_cycles', 'harvest_amount', 'total_feed')
    list_filter = ('farm',)
    fieldsets = (
        (None, {'fields': ('farm', 'harvest_amount')}),
        ('FarmAnalytics info', {'fields': ('no_of_cycles', 'total_feed', 'extra_info', )}),
       )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('farm', 'no_of_cycles', 'extra_info', 'harvest_amount'),
        }),
    )
    search_fields = ('farm',)
    ordering = ('farm',)
    filter_horizontal = ()


class FarmCertificatesAdmin(admin.ModelAdmin):

    list_display = ('certificates','certificate_name', 'certificate_number', )
    list_filter = ('certificates',)
    fieldsets = (
        (None, {'fields': ('certificate_name', 'certificate_number')}),
        ('Cerificates info', {'fields': ('add_information', 'image', 'certificates', )}),
       )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('certificate_name', 'certificate_number', 'certificates', 'add_information'),
        }),
    )
    search_fields = ('certificate_name',)
    ordering = ('certificate_name',)
    filter_horizontal = ()


class FarmImagesAdmin(admin.ModelAdmin):

    list_display = ('image','images')
    list_filter = ('images',)
    fieldsets = (
        (None, {'fields': ('image_name', 'image', 'images', )}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('image_name', 'images',),
        }),
    )
    search_fields = ('image_name',)
    ordering = ('images',)
    filter_horizontal = ()


class FeedLotsAdmin(admin.ModelAdmin):

    list_display = ('farm_id', 'lot_number',)
    list_filter = ('farm_id', )
    fieldsets = (
        (None, {'fields': ('farm_id', 'lot_number', 'company_purchased_from', 'date_purchased', 'date_shipped')}),
        ('FeedLots info', {'fields': ('date_received', 'bag_is_used', 'feed_cost', 'currency', 'feed_lot_type')}),
       )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('farm_id', 'company_purchased_from', 'lot_number', 'currency'),
        }),
    )
    search_fields = ('lot_number',)
    ordering = ('lot_number',)
    filter_horizontal = ()


admin.site.register(Farms, FarmsAdmin)
admin.site.register(FarmImage, FarmImagesAdmin)
admin.site.register(FarmCertification, FarmCertificatesAdmin)
admin.site.register(FeedLots, FeedLotsAdmin)
admin.site.register(FarmAnalytics, FarmAnalyticsAdmin)
