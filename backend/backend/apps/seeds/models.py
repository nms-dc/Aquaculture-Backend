from locale import currency
from re import I
from django.db import models
from accounts.models import User
from company.models import Company
from species.models import Species
from farms.models import Farms


class SeedPlStage(models.Model):
    type = models.CharField(max_length=250, null=True)
    type_description = models.CharField(max_length=250, null=True)


class Seeds(models.Model):

    lot_number = models.CharField(max_length=24, default=None, null=True, blank=True)
    date_received = models.CharField(max_length=400, null=True, blank=True)
    number_of_eggs = models.IntegerField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True)
    date_sold = models.DateTimeField(blank=True)
    date_hatched = models.DateTimeField(blank=True)
    qr_code_id = models.IntegerField(null=True, blank=True)
    quality = models.CharField(max_length=400, null=True, default='good', blank=True)
    weight = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, default=None, null=True, blank=True)
    seed_company_id = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True, blank=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, default=None, null=True, blank=True)
    species_pl_stage = models.ForeignKey(SeedPlStage, on_delete=models.CASCADE, default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seed_user_create', default=None, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seed_user_update', default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class SeedImage(models.Model):
    image = models.FileField(upload_to='seedpicture_uploads', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    fish_ids = models.ForeignKey(Seeds, on_delete=models.CASCADE, related_name='fish_id', default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id)

