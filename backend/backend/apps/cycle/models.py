from locale import currency
from django.db import models
from ponds.models import Ponds,PondImage
from species.models import Species
from seeds.models import Seeds
from harvests.models import Harvests
from common.models import Currency
from company.models import Company

species_choice = (
    ('1' , 'Vennamai'),
     
)

pl_choice = (
    ('1','PL-5'),
    ('2', 'PL-10'),
    ('3', 'PL-15') 
     
)


# Create your models here.
class Cycle(models.Model):

    Pond = models.ForeignKey(Ponds, on_delete=models.CASCADE, default = None,null=True)
    species = models.CharField(max_length = 400, null = True, choices = species_choice, default='1')
    speciesPlStage = models.CharField(max_length = 400, null = True, choices = pl_choice, default='1')
    seed_company = models.ForeignKey(Company, on_delete=models.CASCADE, default = None,null=True)
    invest_amount = models.IntegerField(null = True, default = 0)
    pondPrep_cost = models.IntegerField(null = True, default = 0)
    description = models.CharField(max_length = 400, null = True)
    lastupdatedt = models.DateField(auto_now = True)
    seed_image = models.FileField(upload_to = 'harvestpicture_uploads', null=True)
    pond_image = models.FileField(upload_to = 'harvestpicture_uploads', null=True)
    seeding_date = models.DateField(auto_now = True)
    
    def __str__(self) -> str:
        return self.species
    

class CyclePondImage(models.Model):

    image_name = models.CharField(max_length = 400, null = True)
    image = models.FileField(upload_to = 'pond_images', null=True)
    images = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name = 'pond_images', default = None,null=True)    
    

class CycleSeedImage(models.Model):

    image_name = models.CharField(max_length = 400, null = True)    
    image = models.FileField(upload_to = 'seed_images', null=True)
    images = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name = 'seed_images', default = None,null=True)    
    

