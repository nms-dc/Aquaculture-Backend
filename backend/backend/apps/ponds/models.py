from django.db import models

# Create your models here.

class PondType(models.Model):
    name = models.CharField(max_length=24, default = None)
    desc = models.CharField(max_length=24, default = None)


class PondConstructType(models.Model):
    
    construct_type = models.CharField(max_length=24, default = None,null=True)


class Ponds(models.Model):
        
    pond_name = models.CharField(max_length=240, default = None)
    pond_length = models.FloatField(null=True)
    pond_depth = models.FloatField(null=True)
    pond_breadth = models.FloatField(null=True)
    pond_area  = models.FloatField(null=True)
    pond_capacity = models.FloatField(null=True)
    pond_type = models.ForeignKey(PondType, on_delete=models.CASCADE,related_name = 'pond_types', null=True)
    pond_construct_type = models.ForeignKey(PondConstructType, on_delete=models.CASCADE,related_name = 'pond_construct_types', null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    description = models.CharField(max_length=240, default = None)
    createdAt = models.DateField(auto_now = True,null=True)
    lastupdatedt = models.DateField(auto_now = True,null=True)
    pond_number = models.IntegerField(default=0,null=True)
    last_feed_datetime = models.DateField(auto_now = True,null=True)
    last_preparation_time = models.DateField(auto_now = True,null=True)
    last_stock_date = models.DateField(auto_now = True,null=True) 
    current_stock_id = models.IntegerField(default=0,null=True)
    estimated_harvest_date = models.DateField(auto_now = True,null=True)
    farm = models.ForeignKey('farms.Farms', on_delete=models.CASCADE,related_name = 'farm', default = None, null=True)

    def __str__(self):

        return self.pond_name

class PondImage(models.Model):
    image = models.FileField(upload_to = 'pond_images', null=True)
    image_name = models.CharField(max_length=24, default = None, null = True)
    images = models.ForeignKey(Ponds, on_delete = models.CASCADE, related_name = 'pond_images', null = True)

    