from django.db import models

# Create your models here.

class FarmImage(models.Model):
    image = models.ImageField(upload_to = 'uploads', height_field = None, width_field = None)
    user = models.CharField(max_length=24, default = None)

class FarmCertification(models.Model):

    certificate_name = models.CharField(max_length=24, default = None)
    certificate_number = models.IntegerField(default=0)
    add_information = models.TextField(max_length=224, default = None)
    image = models.ImageField(upload_to = 'uploads')


class Farms(models.Model):

    #user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    company_id = models.IntegerField(default=0)
    farm_name = models.CharField(max_length=24, default = None,null=True)
    farm_area = models.IntegerField(default=0,null=True)
    phone = models.IntegerField(default=0,null=True)
    address_line_one = models.TextField(max_length=224, default = None,null=True)
    address_line_two = models.TextField(max_length=224, default = None,null=True)
    city = models.CharField(max_length=24, default = None,null=True)
    country = models.CharField(max_length=24, default = None,null=True)
    town_village = models.CharField(max_length=24, default = None,null=True)
    zipcode = models.IntegerField(default=0,null=True)
    state = models.CharField(max_length=24, default = None,null=True)
    lat = models.IntegerField(default=0,null=True)
    lng = models.IntegerField(default=0,null=True)
    description = models.TextField(max_length=224, default = None,null=True)
    lastupdatedt = models.DateField(auto_now= True,null=True)
    createdAt = models.DateField(auto_now= True,null=True)
    #image = models.ForeignKey(FarmImage, on_delete=models.CASCADE,related_name='images',null=True,blank=True)
    certificate = models.ForeignKey(FarmCertification, on_delete=models.CASCADE,related_name='certificate',null=True, blank=True)
    farm_status = models.CharField(max_length=24, default = None,null=True)
    

    #this model has many to many reference with user model


    def __str__(self):

        return self.farm_name