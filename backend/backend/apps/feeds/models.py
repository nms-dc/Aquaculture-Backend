from django.db import models

# Create your models here.
class FeedHistories(models.Model):
    updatedAt = models.DateField(auto_now= True)
    feed_id = models.IntegerField(default=0)
    pond_id = models.IntegerField(default=0)
    feed_date = models.DateField(auto_now= True)
    feed_amount = models.FloatField(null=True)
    createdAt = models.DateField(auto_now= True)
    createdAt = models.DateField(auto_now= True)
    feed_id = models.IntegerField(default=0)
    feed_type = models.CharField(max_length=24, default = None)
    updatedAt = models.DateField(auto_now= True)


class Feeds(models.Model):

    user_lat = models.IntegerField(default=0)
    user_llong = models.IntegerField(default=0)
    updatedAt = models.DateField(auto_now= True)
    createdAt = models.DateField(auto_now= True)
    date_used = models.DateField(auto_now= True)
    quality = models.TextField(max_length=224, default = None)
    current_weight = models.IntegerField(default=0)
    weight_at_purchase = models.IntegerField(default=0)
    farm_id = models.IntegerField(default=0)
    company_purchased_from = models.CharField(max_length=24, default = None)
    delivery_date = models.DateField(auto_now= True)
    purchase_date = models.DateField(auto_now= True)
    currency_id = models.IntegerField(default=0)
    feed_cost = models.IntegerField(default=0)
    feed_type_id = models.IntegerField(default=0)
    feed_name = models.CharField(max_length=24, default = None)
    pictures = models.ImageField(upload_to = None, height_field = None, width_field = None)
    public_id = models.IntegerField(default=0)
    qr_code_id = models.IntegerField(default=0)
    created_by_user_id = models.IntegerField(default=0)
    #FeedHistories Model has ForeignKey reference with this model but dont know where it will come

    
    def __str__(self):

        return self.feed_name


