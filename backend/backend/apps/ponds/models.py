from django.db import models

# Create your models here.
class PondConstructType(models.Model):
    pond_construct_type = models.CharField(max_length=24, default = None)

class PondType(models.Model):
    name = models.CharField(max_length=24, default = None)
    desc = models.CharField(max_length=24, default = None)

class PondImage(models.Model):
    image = models.ImageField(upload_to = 'uploads', height_field = None, width_field = None)
    user = models.CharField(max_length=24, default = None)


class Ponds(models.Model):

    pond_type = models.CharField(max_length=24, default = None)
    pond_name = models.CharField(max_length=24, default = None)
    pond_length = models.FloatField(null=True)
    pond_depth = models.FloatField(null=True)
    pond_breadth = models.FloatField(null=True)
    pond_area  = models.FloatField(null=True)
    pond_capacity = models.FloatField(null=True)
    lat = models.ManyToManyField('accounts.User', related_name='User')
    lng = models.FloatField(null=True)
    description = models.CharField(max_length=24, default = None)
    current_aquaculture_growing_id = models.IntegerField(default=0)
    createdAt = models.DateField(auto_now = True)
    lastupdatedt = models.DateField(auto_now = True)
    image = models.ForeignKey(PondImage, on_delete=models.CASCADE)
    user = models.CharField(max_length=24, default = None)
    pond_number = models.IntegerField(default=0)
    last_feed_datetime = models.DateField(auto_now = True)
    last_preparation_time = models.DateField(auto_now = True)
    last_stock_date = models.ForeignKey('cycle.Cycle', on_delete=models.CASCADE) 
    current_stock_id = models.IntegerField(default=0)
    estimated_harvest_date = models.DateField(auto_now = True)
    pond_construct_type = models.OneToOneField(PondConstructType,on_delete=models.CASCADE)

    #this model has foreign key reference with pond type but dont know the field
    #this model has foreign key reference with Farms but dont know the field


    def __str__(self):

        return self.pond_name

    