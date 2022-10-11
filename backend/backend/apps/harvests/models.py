from re import T
from django.db import models
from ponds.models import Ponds, PondImage
from company.models import Company


class Harvests(models.Model):

    HARVEST_TYPE = (
        ('F', 'Full Harvest'),
        ('P', 'Partial Harvest')
    )
    harvest_type = models.CharField(max_length=400, choices=HARVEST_TYPE, default='F', null=True)
    total_kgs = models.IntegerField(null=True, default=0)
    is_chill_kill = models.BooleanField(default=True)
    harvest_date = models.DateField(auto_now=True)
    temperature = models.IntegerField(null=True, default=0)
    sold_to = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)
    harvest_notes = models.CharField(max_length=400, null=True, default='1')
    harvest_cost = models.IntegerField(null=True, default=0)
    cycle = models.ForeignKey('cycle.Cycle', on_delete=models.CASCADE, default=None, null=True)
    animal_count_1 = models.IntegerField(null=True, default=0)
    total_kg_1 = models.IntegerField(null=True, default=0)
    price_kg_1 = models.IntegerField(null=True, default=0)

    def __str__(self) -> str:
        return self.harvest_type


class AddAnimal(models.Model):

    animal_count = models.IntegerField(null=True, default=0)
    total_kg = models.IntegerField(null=True, default=0)
    price_kg = models.IntegerField(null=True, default=0)
    adding_animal = models.ForeignKey(Harvests, on_delete=models.CASCADE, related_name='animal_images', default=None, null=True)


class HarvestAnimalImages(models.Model):

    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='ani_images', null=True)
    images = models.ForeignKey(Harvests, on_delete=models.CASCADE, related_name='ani_images', default=None, null=True)


class HarvestPondImages(models.Model):

    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='pond_images', null=True)
    images = models.ForeignKey(Harvests, on_delete=models.CASCADE, related_name='pond_images', default=None, null=True)


class HarvestLogisticImages(models.Model):

    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='log_images', null=True)
    images = models.ForeignKey(Harvests, on_delete=models.CASCADE, related_name='log_images', default=None, null=True)
