
from email.policy import default
from pyexpat import model
from django.db import models
from numpy import record
from company.models import Company
from cycle.models import Cycle
from django.utils import timezone
from farms.models import FeedLots


class MeasurementMaster(models.Model):
    measurement_type = models.CharField(max_length=400, null=True)
    measurement_description = models.CharField(max_length=400, null=True)

    def __str__(self):
        return str(self.measurement_type)


class Measurement(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, default=None, null=True)
    value = models.FloatField(null=True)
    time = models.DateTimeField(default=timezone.now)
    lot = models.ForeignKey(FeedLots, on_delete=models.CASCADE, default=None, null=True)
    price_per_kg = models.IntegerField(null=True)
    measurement_type = models.ForeignKey(MeasurementMaster, on_delete=models.CASCADE, default=None, null=True)
    is_probiotic_mixed = models.BooleanField(default=False)
    notes = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Nutrition(models.Model):
    nutrition = models.CharField(max_length=400, null=True)
    nutrition_type = models.CharField(max_length=400, null=True)
    nutrition_description = models.CharField(max_length=400, null=True)
    feed_data = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='nutrition_data', default=None, null=True)

    def __str__(self):
        return str(self.nutrition)


class MeasurementPics(models.Model):
    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='measure_images', null=True)
    images = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='measure_images', default=None, null=True)

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name_plural = "MeasurementPics"
		