from django.db import models

# Create your models here.

   


class Ponds(models.Model):
        
    pond_name = models.CharField(max_length=240, default = None)
    pond_length = models.FloatField(null=True)
    pond_depth = models.FloatField(null=True)
    pond_breadth = models.FloatField(null=True)
    pond_area  = models.FloatField(null=True)
    pond_capacity = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    description = models.CharField(max_length=240, default = None)
    current_aquaculture_growing_id = models.IntegerField(default=0,null=True)
    createdAt = models.DateField(auto_now = True,null=True)
    lastupdatedt = models.DateField(auto_now = True,null=True)
    user = models.CharField(max_length=240, default = None,null=True)
    pond_number = models.IntegerField(default=0,null=True)
    last_feed_datetime = models.DateField(auto_now = True,null=True)
    last_preparation_time = models.DateField(auto_now = True,null=True)
    last_stock_date = models.DateField(auto_now = True,null=True) 
    current_stock_id = models.IntegerField(default=0,null=True)
    estimated_harvest_date = models.DateField(auto_now = True,null=True)
    

    def __str__(self):

        return self.pond_name

class PondType(models.Model):
    name = models.CharField(max_length=24, default = None)
    desc = models.CharField(max_length=24, default = None)
    pond_type = models.ForeignKey(Ponds, on_delete=models.CASCADE,related_name = 'pond_types', null=True)
    #related name one of the most important attribute for nested serializer

class PondConstructType(models.Model):
    
    construct_type = models.CharField(max_length=24, default = None,null=True)
    Pond_ConstructTypes = models.ForeignKey(Ponds, on_delete = models.CASCADE, related_name = 'PondConstructTypes',  null=True)

class PondImage(models.Model):
    image = models.ImageField(upload_to = 'uploads', null=True)
    user = models.CharField(max_length=24, default = None,null=True)    
    images = models.ForeignKey(Ponds, on_delete = models.CASCADE, related_name = 'pond_images', null = True)

    