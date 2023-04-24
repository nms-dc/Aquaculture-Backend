from django.contrib import admin
from farms.models import Farms, FarmImage, FarmCertification, FeedLots, FarmAnalytics, FeedLotTypes, FarmUser


# Register your models here.

class FarmsAdmin(admin.ModelAdmin):

    list_display = ('farm_name', 'farm_area', 'company_id')
    list_filter = ('company_id', 'farm_name', )
    fieldsets = (
        (None, {'fields': ('company_id', 'farm_name')}),
        ('Farm info', {'fields': (('farm_area', 'phone'), 'description',)}),
        ('Address info', {'fields': ('city', 'country', 'town_village', 'zipcode', 'state', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company_id', 'farm_area', 'farm_name'),
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
    def farm_name(self,obj):
        return obj.farm_id

    list_display = ('farm_name','certificate_name', 'certificate_number', )
    list_filter = ('certificate_name',)
    fieldsets = (
        (None, {'fields': ('certificate_name', 'certificate_number')}),
        ('Cerificates info', {'fields': ('add_information', 'image', 'farm_id', )}),
       )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('certificate_name', 'certificate_number', 'farm_id', 'add_information'),
        }),
    )
    search_fields = ('certificate_name',)
    ordering = ('certificate_name',)
    filter_horizontal = ()


class FarmImagesAdmin(admin.ModelAdmin):

    def farm_name(self,obj):
        return obj.images.farm_name


    list_display = ('farm_name','image',)
    list_filter = ('image_name',)
    fieldsets = (
        (None, {'fields': ('image_name', 'image', 'images', )}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('image_name', 'farm_name',),
        }),
    )
    search_fields = ('image_name',)
    ordering = ('images',)
    filter_horizontal = ()


class FeedLotsAdmin(admin.ModelAdmin):

    def farm_name(self,obj):
        return obj.farm_id.farm_name

    list_display = ('farm_name', 'lot_number',"feed_lot_type", "company_feed_type")
    list_filter = ('feed_lot_type', )
    fieldsets = (
        (None, {'fields': ('farm_id', 'lot_number', 'company_purchased_from', 'date_purchased', 'date_shipped')}),
        ('FeedLots info', {'fields': ('date_received', 'bag_is_used', 'feed_cost', 'currency', 'feed_lot_type')}),
       )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('farm_name', 'company_purchased_from', 'lot_number', 'currency'),
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
admin.site.register(FeedLotTypes)
admin.site.register(FarmUser)
