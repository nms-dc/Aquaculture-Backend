from django.db import models

# Create your models here.
class CyclePondImage(models.Model):
    image = models.ImageField(upload_to = 'uploads', height_field = None, width_field = None)
    user = models.CharField(max_length=24, default = None)

    def __str__(self):

        return self.user

class Cycle(models.Model):
    pond = models.ForeignKey('ponds.Ponds', on_delete=models.CASCADE) 
    species =  models.ForeignKey('species.Species', on_delete=models.CASCADE)
    seed_company = models.ForeignKey('seeds.Seeds', on_delete=models.CASCADE)
    invest_amount = models.IntegerField(default=0)
    pond_prep_cost = models.IntegerField(default=0)
    address_line_two = models.TextField(max_length=224, default = None)
    description = models.TextField(max_length=224, default = None)
    lastupdatedt = models.DateField(auto_now= True)
    seed_image = models.ForeignKey('seeds.SeedImage', on_delete=models.CASCADE)
    pond_image = models.ForeignKey(CyclePondImage, on_delete=models.CASCADE)
    harvest_id = models.OneToOneField('harvests.Harvests',on_delete=models.CASCADE)
    sold_to = models.CharField(max_length=24, default = None)
    process_date = models.DateField(auto_now= True)
    company_id = models.IntegerField(default=0)
    createdAt = models.DateField(auto_now= True)
    sold_amount = models.FloatField(null=True)
    currency_id = models.DateField(auto_now= True)
    #this model has foreign key reference from Measurement historeis dont know the field
    #this model has one to one field with harvest model but not sure about the fields

    def __str__(self):

        return self.pond
        