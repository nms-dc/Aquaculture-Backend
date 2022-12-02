from email.policy import default
from pyexpat import model
from django.db import models
from numpy import record
from company.models import Company
from cycle.models import Cycle
from django.utils import timezone


# Create your models here.
class MeasurementMaster(models.Model):
    measurement_type = models.CharField(max_length=400, null=True)
    measurement_description = models.CharField(max_length=400, null=True)


class Measurement(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, default=None, null=True)
    value = models.FloatField(null=True)
    # time = models.TimeField(null=True)
    time = models.DateTimeField(default=timezone.now)
    # time = models.TimeField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)
    price_per_kg = models.IntegerField(null=True)
    measurement_type = models.ForeignKey(MeasurementMaster, on_delete=models.CASCADE, default=None, null=True)
    

    

    


class Nutrition(models.Model):
    nutrition = models.CharField(max_length=400, null=True)
    nutrition_type = models.CharField(max_length=400, null=True)
    nutrition_description = models.CharField(max_length=400, null=True)
    feed_data = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='nutrition_data', default=None, null=True)


class MeasurementPics(models.Model):
    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='measure_images', null=True)
    images = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='measure_images', default=None, null=True)
