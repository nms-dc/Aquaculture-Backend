from locale import currency
from django.db import models
from ponds.models import Ponds, PondImage
from farms.models import Farms
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

    Pond = models.ForeignKey(Ponds, on_delete=models.CASCADE, related_name='pond_description', default=None, null=True)
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
    doc = models.IntegerField(null=True)
    seed_transfer_date = models.DateField(default=None, null=True)
    is_active = models.BooleanField(default=True)
    pond_transfered_from = models.ForeignKey(Ponds, on_delete=models.CASCADE,related_name='pond_availability', default=None, null=True)


    def __str__(self):
        return str(self.species)


class CyclePondImage(models.Model):

    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='cycle_pond_images', null=True)
    images = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='cycle_pond_images', default=None, null=True)


class CycleSeedImage(models.Model):

    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='cycle_seed_images', null=True)
    images = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='seed_images', default=None, null=True)


def get_default_info():
    return {'measurement_id': None}


class CycleAnalytics(models.Model):
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, related_name='cycle_farm_analytics')
    pond = models.ForeignKey(Ponds, on_delete=models.CASCADE, related_name='cycle_pond_analytics', null=True)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='cycle_analytics', default=None, null=True)
    harvest_amount = models.FloatField(null=True, blank=True)
    total_feed = models.FloatField(null=True, blank=True)
    extra_info = models.JSONField(null=True, blank=True, default=get_default_info)


    class Meta:
        verbose_name_plural = "CycleAnalytics"    
