from django.db import models

# Create your models here.
class SeedImage(models.Model):
    image = models.ImageField(upload_to = '/uploads', height_field = None, width_field = None)
    user = models.CharField(max_length=24, default = None)

class Seeds(models.Model):
    public_id = models.IntegerField(default=0)
    date_received = models.DateField(auto_now= True)
    number_of_eggs = models.IntegerField(default=0)
    updatedAt = models.DateField(auto_now= True)
    createdAt = models.DateField(auto_now= True)
    date_sold = models.DateField(auto_now= True)
    date_hatched = models.DateField(auto_now= True)
    qr_code_id = models.IntegerField(default=0)
    quality = models.TextField(max_length=224, default = None)
    fish_id = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    currency_id = models.IntegerField(default=0)
    price = models.FloatField(null=True)
    purchased_company_id = models.IntegerField(default=0)
    seed_company_id = models.IntegerField(default=0)

    #this model is getting foreign key reference from Seed Image dont know where    
    def __str__(self):

        return self.quality
