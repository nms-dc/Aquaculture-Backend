from django.db import models
from company.models import Company, CompanyFeedType
from common.models import Currency
from accounts.models import User, Roles


class Farms(models.Model):

    company_id = models.IntegerField(default=0)
    farm_name = models.CharField(max_length=24, default=None, null=True)
    farm_area = models.FloatField(null=True, blank=True)
    phone = models.CharField(max_length=24, default=None, null=True)
    address_line_one = models.TextField(max_length=224, default=None, null=True)
    address_line_two = models.TextField(max_length=224, default=None, null=True)
    city = models.CharField(max_length=24, default=None, null=True)
    country = models.CharField(max_length=24, default=None, null=True)
    town_village = models.CharField(max_length=24, default=None, null=True)
    zipcode = models.CharField(max_length=24, default=None, null=True)
    state = models.CharField(max_length=24, default=None, null=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=224, default=None, null=True)
    lastupdatedt = models.DateField(auto_now=True, null=True)
    createdAt = models.DateField(auto_now=True, null=True)
    district = models.CharField(max_length=24, default=None, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farm_user_create', default=None, null=True)
    created_at = models.DateField(auto_now=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farm_user_update', default=None, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return 'farm_id:'+' '+str(self.id)
    
    class Meta:
        verbose_name_plural = "Farms"


class FarmImage(models.Model):

    image = models.FileField(upload_to='farmimage_uploads', null=True)
    image_name = models.CharField(max_length=24, default=None, null=True)
    images = models.ForeignKey(Farms, on_delete=models.CASCADE, related_name='farm_images', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fimage_user_create', default=None, null=True)
    created_at = models.DateField(auto_now=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fimage_user_update', default=None, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return str(self.image)

class FarmCertification(models.Model):

    certificate_name = models.CharField(max_length=24, default=None, null=True)
    certificate_number = models.IntegerField(default=0, null=True)
    add_information = models.TextField(max_length=224, default=None, null=True)
    image = models.ImageField(upload_to='certificate_uploads', null=True)
    farm_id = models.ForeignKey(Farms, on_delete=models.CASCADE, related_name='certificate', null=True, blank=True)
    expiry_date = models.DateField(default=None, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fcerti_user_create', default=None, null=True)
    created_at = models.DateField(auto_now=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fcerti_user_update', default=None, null=True)
    updated_at = models.DateField(auto_now=True, null=True)


    def __str__(self):
        return str(self.certificate_name)


class FeedLotTypes(models.Model):
    lot_type = models.CharField(max_length=24, default=None, null=True)
    lot_type_description = models.CharField(max_length=24, default=None, null=True)


class FeedLots(models.Model):
    
    farm_id = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, blank=True)
    lot_number = models.CharField(max_length=24, default=None, null=True)
    company_purchased_from = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    weight_of_each_bag_at_purchase = models.FloatField(default=0, null=True)
    date_purchased = models.DateField(null=True)
    date_shipped = models.DateField(null=True)
    date_received = models.DateField(null=True)
    bag_is_used = models.BooleanField(default=False)
    feed_cost = models.FloatField(null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    feed_lot_type = models.ForeignKey(FeedLotTypes, on_delete=models.CASCADE, null=True, blank=True)
    company_feed_type = models.ForeignKey(CompanyFeedType, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flot_user_create', default=None, null=True)
    created_at = models.DateField(auto_now=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flot_user_update', default=None, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return str(self.feed_lot_type)

def get_default_info():
    return {'measurement_id': None}


class FeedLotImage(models.Model):

    image = models.FileField(upload_to='feedlot_uploads', null=True)
    image_name = models.CharField(max_length=24, default=None, null=True)
    images = models.ForeignKey(FeedLots, on_delete=models.CASCADE, related_name='feed_images', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='felimage_user_create', default=None, null=True)
    created_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='felimage_user_update', default=None, null=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)


class FarmAnalytics(models.Model):
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, related_name='farm_analytics')
    no_of_cycles = models.IntegerField(default=0,  null=True)
    harvest_amount = models.FloatField(null=True, blank=True)
    total_feed = models.FloatField(null=True, blank=True)
    extra_info = models.JSONField(null=True, blank=True, default=get_default_info)

    def __str__(self):
       return str(self.id)
    
    class Meta:
        verbose_name_plural = "FarmAnalytics"


class FarmUser(models.Model):
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, related_name='farm_record')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_record')
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True, related_name='role_record')
