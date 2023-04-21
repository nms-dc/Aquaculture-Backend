from locale import currency
from re import I
from django.db import models
from accounts.models import User
from company.models import Company
from species.models import Species


class SeedPlStage(models.Model):
    type = models.CharField(max_length=250, null=True)
    type_description = models.CharField(max_length=250, null=True)


class Seeds(models.Model):

    lot_number = models.CharField(max_length=24, default=None, null=True)
    date_received = models.CharField(max_length=400, null=True)
    number_of_eggs = models.IntegerField(null=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    date_sold = models.DateTimeField()
    date_hatched = models.DateTimeField()
    qr_code_id = models.IntegerField(null=True)
    quality = models.CharField(max_length=400, null=True, default='good')
    weight = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    seed_company_id = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, default=None, null=True)
    species_pl_stage = models.ForeignKey(SeedPlStage, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return str(self.id)


class SeedImage(models.Model):
    image = models.FileField(upload_to='seedpicture_uploads', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    fish_ids = models.ForeignKey(Seeds, on_delete=models.CASCADE, related_name='fish_id', default=None, null=True)

    def __str__(self):
        return str(self.id)

