from django.db import models
from company.models import Company, CompanyFeedType
from common.models import Currency
from accounts.models import User, Roles


class Farms(models.Model):

    company_id = models.IntegerField(default=0, blank=True)
    farm_name = models.CharField(max_length=24, default=None, null=True, blank=True)
    farm_area = models.FloatField(null=True, blank=True)
    phone = models.CharField(max_length=24, default=None, null=True, blank=True)
    address_line_one = models.TextField(max_length=224, default=None, null=True, blank=True)
    address_line_two = models.TextField(max_length=224, default=None, null=True, blank=True)
    city = models.CharField(max_length=24, default=None, null=True, blank=True)
    country = models.CharField(max_length=24, default=None, null=True, blank=True)
    town_village = models.CharField(max_length=24, default=None, null=True, blank=True)
    zipcode = models.CharField(max_length=24, default=None, null=True, blank=True)
    state = models.CharField(max_length=24, default=None, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=224, default=None, null=True, blank=True)
    lastupdatedt = models.DateField(auto_now=True, null=True, blank=True)
    createdAt = models.DateField(auto_now=True, null=True, blank=True)
    district = models.CharField(max_length=24, default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farm_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farm_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'farm_id:'+' '+str(self.id)
    
    class Meta:
        verbose_name_plural = "Farms"


class FarmImage(models.Model):

    image = models.FileField(upload_to='farmimage_uploads', null=True, blank=True)
    image_name = models.CharField(max_length=24, default=None, null=True, blank=True)
    images = models.ForeignKey(Farms, on_delete=models.CASCADE, related_name='farm_images', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fimage_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fimage_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.image)

class FarmCertification(models.Model):

    certificate_name = models.CharField(max_length=24, default=None, null=True, blank=True)
    certificate_number = models.IntegerField(default=0, null=True, blank=True)
    add_information = models.TextField(max_length=224, default=None, null=True, blank=True)
    image = models.ImageField(upload_to='certificate_uploads', null=True, blank=True)
    farm_id = models.ForeignKey(Farms, on_delete=models.CASCADE, related_name='certificate', null=True, blank=True)
    expiry_date = models.DateField(default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fcerti_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fcerti_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)


    def __str__(self):
        return str(self.certificate_name)


class FeedLotTypes(models.Model):
    lot_type = models.CharField(max_length=24, default=None, null=True, blank=True)
    lot_type_description = models.CharField(max_length=24, default=None, null=True, blank=True)


class FeedLots(models.Model):
    
    farm_id = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, blank=True)
    lot_number = models.CharField(max_length=24, default=None, null=True, blank=True)
    company_purchased_from = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    weight_of_each_bag_at_purchase = models.FloatField(default=0, null=True, blank=True)
    date_purchased = models.DateField(null=True, blank=True)
    date_shipped = models.DateField(null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    bag_is_used = models.BooleanField(default=False, blank=True)
    feed_cost = models.FloatField(null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    feed_lot_type = models.ForeignKey(FeedLotTypes, on_delete=models.CASCADE, null=True, blank=True)
    company_feed_type = models.ForeignKey(CompanyFeedType, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flot_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flot_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.feed_lot_type)

def get_default_info():
    return {'measurement_id': None}


class FeedLotImage(models.Model):

    image = models.FileField(upload_to='feedlot_uploads', null=True, blank=True)
    image_name = models.CharField(max_length=24, default=None, null=True, blank=True)
    images = models.ForeignKey(FeedLots, on_delete=models.CASCADE, related_name='feed_images', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='felimage_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='felimage_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class FarmAnalytics(models.Model):
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, related_name='farm_analytics', blank=True)
    no_of_cycles = models.IntegerField(default=0,  null=True, blank=True)
    harvest_amount = models.FloatField(null=True, blank=True)
    total_feed = models.FloatField(null=True, blank=True)
    extra_info = models.JSONField(null=True, blank=True, default=get_default_info)

    def __str__(self):
       return str(self.id)
    
    class Meta:
        verbose_name_plural = "FarmAnalytics"


class FarmUser(models.Model):
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, related_name='farm_record', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_record', blank=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True, related_name='role_record', blank=True)
