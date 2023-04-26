from re import T
from django.db import models
from ponds.models import Ponds, PondImage
from company.models import Company
from accounts.models import User


class Harvests(models.Model):

    HARVEST_TYPE = (
        ('F', 'Full Harvest'),
        ('P', 'Partial Harvest')
    )
    harvest_type = models.CharField(max_length=400, choices=HARVEST_TYPE, default='F', null=True, blank=True)
    total_kgs = models.FloatField(null=True, default=0, blank=True)
    is_chill_kill = models.BooleanField(default=True, blank=True)
    harvest_date = models.DateField(auto_now=True, blank=True)
    temperature_celcius = models.FloatField(null=True, default=0, blank=True)
    sold_to = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True, blank=True)
    harvest_notes = models.CharField(max_length=400, null=True, default='1', blank=True)
    harvest_cost = models.FloatField(null=True, default=0, blank=True)
    cycle = models.ForeignKey('cycle.Cycle', on_delete=models.CASCADE, default=None, null=True, blank=True)
    animal_count_1 = models.IntegerField(null=True, default=0, blank=True)
    harvest_quality = models.IntegerField(null=True, default=0, blank=True)
    total_kg_1 = models.FloatField(null=True, default=0, blank=True)
    price_kg_1 = models.FloatField(null=True, default=0, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='harvest_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='harvest_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.harvest_type


class AddAnimal(models.Model):

    animal_count = models.IntegerField(null=True, default=0, blank=True)
    total_kg = models.FloatField(null=True, default=0, blank=True)
    price_kg = models.FloatField(null=True, default=0, blank=True)
    adding_animal = models.ForeignKey(Harvests, on_delete=models.CASCADE, related_name='animal_images', default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id)



class HarvestAnimalImages(models.Model):

    image_name = models.CharField(max_length=400, null=True, blank=True)
    image = models.FileField(upload_to='harvest_animal_images', null=True, blank=True)
    images = models.ForeignKey(Harvests, on_delete=models.CASCADE, related_name='ani_images', default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='haimage_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='haimage_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.image_name)


class HarvestPondImages(models.Model):

    image_name = models.CharField(max_length=400, null=True, blank=True)
    image = models.FileField(upload_to='harvest_pond_images', null=True, blank=True)
    images = models.ForeignKey(Harvests, on_delete=models.CASCADE, related_name='pond_images', default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hpimage_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hpimage_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.image_name)


class HarvestLogisticImages(models.Model):

    image_name = models.CharField(max_length=400, null=True, blank=True)
    image = models.FileField(upload_to='harvest_log_images', null=True, blank=True)
    images = models.ForeignKey(Harvests, on_delete=models.CASCADE, related_name='log_images', default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hlimage_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hlimage_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.image_name)
