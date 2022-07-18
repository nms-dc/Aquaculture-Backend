from django.db import models

# Create your models here.
class Harvests(models.Model):
    pond_id = models.IntegerField(default=0)
    final_harvest = models.DateField(auto_now= True)
    createdAt = models.DateField(auto_now= True)
    updatedAt = models.DateField(auto_now= True)
    number_of_fish = models.IntegerField(default=0)
    partial_amount = models.FloatField(null=True)
    fish_id = models.IntegerField(default=0)
    total_kgs = models.FloatField(null=True)
    harvest_start_time = models.TimeField()
    currency_id = models.IntegerField(default=0)
    pond_at_harvest = models.CharField(max_length=24, default = None)
    public_id = models.IntegerField(default=0)
    harvest_quality = models.CharField(max_length=24, default = None)
    company_harvest_sent_to = models.CharField(max_length=24, default = None)
    partial_harvest = models.CharField(max_length=24, default = None)
    qr_code_id = models.IntegerField(default=0)
    user_long = models.FloatField(null=True)
    user_lat = models.FloatField(null=True)
    created_by_user_id = models.DateField(auto_now= True)
    pictures = models.ImageField(upload_to = '/uploads', height_field = None, width_field = None)
    temperature = models.FloatField(null=True)
    vehicle_condition = models.CharField(max_length=24, default = None)
    vehicle_number = models.CharField(max_length=24, default = None)
    load_time = models.TimeField()
    #cycle has one to one relationship with this model

    
    def __str__(self):

        return self.pond_at_harvest

