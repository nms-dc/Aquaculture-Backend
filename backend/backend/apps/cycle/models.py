from locale import currency
from django.db import models
from ponds.models import Ponds, PondImage
from species.models import Species
from seeds.models import Seeds
from harvests.models import Harvests
from common.models import Currency
from company.models import Company
import datetime


class Cycle(models.Model):
    species_choice = (
        (1, 'Vennamai'),
    )

    pl_choice = (
        (1, 'PL-5'),
        (2, 'PL-10'),
        (3, 'PL-15')
    )

    Pond = models.ForeignKey(Ponds, on_delete=models.CASCADE, default=None, null=True)
    species = models.IntegerField(null=True, choices=species_choice, default='1')
    species_pl_stage = models.IntegerField(null=True, choices=pl_choice, default='1')
    seed_company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)
    invest_amount = models.IntegerField(null=True, default=0)
    pondPrep_cost = models.IntegerField(null=True, default=0)
    description = models.CharField(max_length=400, null=True)
    lastupdatedt = models.DateField(auto_now=True)
    seeding_qty = models.IntegerField(default=None, null=True)
    seeding_date = models.DateField(default=datetime.date.today)
    numbers_of_larva = models.IntegerField(default=6000)
    harvest_id = models.IntegerField(null=True)

    def __str__(self):
        return str(self.species)


class CyclePondImage(models.Model):

    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='pond_images', null=True)
    images = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='pond_images', default=None, null=True)


class CycleSeedImage(models.Model):

    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='seed_images', null=True)
    images = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='seed_images', default=None, null=True)
