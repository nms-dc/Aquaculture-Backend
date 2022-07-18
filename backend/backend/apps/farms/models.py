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

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    company_id = models.IntegerField(default=0)
    farm_name = models.CharField(max_length=24, default = None)
    farm_area = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    address_line_one = models.TextField(max_length=224, default = None)
    address_line_two = models.TextField(max_length=224, default = None)
    city = models.CharField(max_length=24, default = None)
    country = models.OneToOneField('common.Countries',on_delete=models.CASCADE)
    town_village = models.CharField(max_length=24, default = None)
    zipcode = models.IntegerField(default=0)
    state = models.CharField(max_length=24, default = None)
    lat = models.IntegerField(default=0)
    lng = models.IntegerField(default=0)
    description = models.TextField(max_length=224, default = None)
    lastupdatedt = models.DateField(auto_now= True)
    createdAt = models.DateField(auto_now= True)
    image = models.ForeignKey(FarmImage, on_delete=models.CASCADE)
    certificate = models.ForeignKey(FarmCertification, on_delete=models.CASCADE)
    farm_status = models.CharField(max_length=24, default = None)

    #this model has many to many reference with user model


    def __str__(self):

        return self.farm_name