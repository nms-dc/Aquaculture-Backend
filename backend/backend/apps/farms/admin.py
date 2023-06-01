from django.contrib import admin
from farms.models import Farms, FarmImage, FarmCertification, FeedLots, FarmAnalytics, FeedLotTypes, FarmUser
from import_export.admin import ExportActionMixin, ImportExportModelAdmin


# Register your models here.

class FarmsAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('farm_name', 'farm_area', 'company_id', 'phone', 'town_village', 'zipcode', 'state', "city", "country")
    list_filter = ('company_id', 'farm_name', )
    fieldsets = (
        (None, {'fields': ('company_id', 'farm_name')}),
        ('Farm info', {'fields': (('farm_area', 'phone'), 'description',)}),
        ('Address info', {'fields': ('town_village', 'zipcode', 'state', "city", "country")}),
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




class FarmAnalyticsAdmin(ImportExportModelAdmin, admin.ModelAdmin):

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


class FarmCertificatesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def farm_name(self,obj):
        return obj.farm_id

    list_display = ('farm_name','certificate_name', 'certificate_number', )
    list_filter = ('certificate_name', 'farm_id')
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


class FarmImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):

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


class FeedLotsAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def farm_name(self,obj):
        return obj.farm_id.farm_name

    list_display = ('farm_name', 'lot_number',"feed_lot_type", "company_feed_type", 'company_purchased_from', 'bag_is_used', 'feed_cost', 'currency')
    list_filter = ('feed_lot_type', 'farm_id', 'company_purchased_from')
    fieldsets = (
        (None, {'fields': ('farm_id', 'lot_number', "company_feed_type", 'company_purchased_from', 'date_purchased', 'date_shipped')}),
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


class FeedLotTypesAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('lot_type','lot_type_description',)
    list_filter = ('lot_type',)
    fieldsets = (
        (None, {'fields': ('lot_type', 'lot_type_description', )}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('lot_type', 'lot_type_description',),
        }),
    )
    search_fields = ('lot_type',)
    ordering = ('lot_type',)
    filter_horizontal = ()


class FarmUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def user_name(self,obj):
        return obj.user.first_name
    
    def farm_name(self,obj):
        return obj.farm.farm_name

    list_display = ('user_name','farm_name', 'role', )
    list_filter = ('farm', 'user')
    fieldsets = (
        (None, {'fields': ('farm', 'user', 'role')}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('farm', 'user', 'role', ),
        }),
    )
    search_fields = ('farm',)
    ordering = ('farm',)
    filter_horizontal = ()

admin.site.register(Farms, FarmsAdmin)
admin.site.register(FarmImage, FarmImagesAdmin)
admin.site.register(FarmCertification, FarmCertificatesAdmin)
admin.site.register(FeedLots, FeedLotsAdmin)
admin.site.register(FarmAnalytics, FarmAnalyticsAdmin)
admin.site.register(FeedLotTypes, FeedLotTypesAdmin)
admin.site.register(FarmUser, FarmUserAdmin)
