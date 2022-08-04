from django.db import models

# Create your models here.
class PondConstructType(models.Model):
    pond_construct_type = models.CharField(max_length=24, default = None)


class PondImage(models.Model):
    image = models.ImageField(upload_to = 'uploads')
    user = models.CharField(max_length=24, default = None)
   

PONDTYPES = (
            ('1','square'),
            ('2','circle'),
            ('3','parabolem'),
            
        )
class Ponds(models.Model):
        
    #select_form = certificate = models.ForeignKey('farms.Farms', on_delete=models.CASCADE,related_name='farm',null=True, blank=True)
    #pond_type = models.CharField(max_length=240,choices = PONDTYPES, default='1')
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
    image = models.ForeignKey(PondImage, on_delete=models.CASCADE, null=True)
    user = models.CharField(max_length=240, default = None,null=True)
    pond_number = models.IntegerField(default=0,null=True)
    last_feed_datetime = models.DateField(auto_now = True,null=True)
    last_preparation_time = models.DateField(auto_now = True,null=True)
    last_stock_date = models.DateField(auto_now = True,null=True) 
    current_stock_id = models.IntegerField(default=0,null=True)
    estimated_harvest_date = models.DateField(auto_now = True,null=True)
    pond_construct_type = models.OneToOneField(PondConstructType,on_delete=models.CASCADE, null=True)

    #this model has foreign key reference with pond type but dont know the field
    #this model has foreign key reference with Farms but dont know the field


    def __str__(self):

        return self.pond_name

class PondType(models.Model):
    name = models.CharField(max_length=24, default = None)
    desc = models.CharField(max_length=24, default = None)
    pond_type = models.ForeignKey(Ponds, on_delete=models.CASCADE,related_name = 'pond_types', null=True)
    #related name one of the most important attribute for nested serializer

    