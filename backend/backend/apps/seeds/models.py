from locale import currency
from re import I
from django.db import models
from accounts.models import User
from company.models import Company


class Seeds(models.Model):

    public_id = models.IntegerField(null=True)
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
    purchased_by_companyid = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)
    seed_company_id = models.IntegerField(null=True)


class SeedImage(models.Model):
    image = models.FileField(upload_to='seedpicture_uploads', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    fish_ids = models.ForeignKey(Seeds, on_delete=models.CASCADE, related_name='fish_id', default=None, null=True)
