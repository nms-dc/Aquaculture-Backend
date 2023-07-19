from locale import currency
from operator import mod
from django.db import models


class Country(models.Model):
    alpha_2_code = models.IntegerField(null=True, blank=True)
    alpha_3_code = models.IntegerField(null=True,  blank=True)
    createdAt = models.DateField(auto_now=True,  blank=True)
    updatedAt = models.DateField(null=True,  blank=True)
    country_name = models.CharField(max_length=400, null=True,  blank=True)
    def __str__(self):
        return str(self.country_name)


class Currency(models.Model):
    createdAt = models.DateField(auto_now=True,  blank=True)
    updatedAt = models.DateField(auto_now=True,  blank=True)
    coutry_id = models.ForeignKey(Country, on_delete=models.CASCADE, default=None, null=True,  blank=True)
    fraction_unit = models.IntegerField(null=True,  blank=True)
    fraction_number = models.IntegerField(null=True,  blank=True)
    iso_code = models.IntegerField(null=True,  blank=True)
    symbol = models.CharField(max_length=400, null=True,  blank=True)
    currency = models.CharField(max_length=400, null=True, default='ruppes',  blank=True)
    def __str__(self):
        return str(self.currency)