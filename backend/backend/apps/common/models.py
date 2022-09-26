from locale import currency
from operator import mod
from django.db import models


class Country(models.Model):
    alpha_2_code = models.IntegerField(null=True)
    alpha_3_code = models.IntegerField(null=True)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now=True)
    country_name = models.CharField(max_length=400, null=True)


class Currency(models.Model):
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now=True)
    coutry_id = models.ForeignKey(Country, on_delete=models.CASCADE, default=None, null=True)
    fraction_unit = models.IntegerField(null=True)
    fraction_number = models.IntegerField(null=True)
    iso_code = models.IntegerField(null=True)
    symbol = models.CharField(max_length=400, null=True)
    currency = models.CharField(max_length=400, null=True, default='ruppes')
