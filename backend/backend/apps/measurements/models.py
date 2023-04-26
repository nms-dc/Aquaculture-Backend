from email.policy import default
from pyexpat import model
from django.db import models
from numpy import record
from company.models import Company
from cycle.models import Cycle
from django.utils import timezone
from farms.models import FeedLots
from accounts.models import User


class MeasurementMaster(models.Model):
    measurement_type = models.CharField(max_length=400, null=True, blank=True)
    measurement_description = models.CharField(max_length=400, null=True, blank=True)
    measurement_logo = models.ImageField(upload_to='measure_type_images', default=None, null=True, blank=True)
    measurement_unit = models.CharField(max_length=100, blank=True, null=True)
    min_limit = models.FloatField(null=True, blank=True)
    max_limit = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.measurement_type)


class Measurement(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, default=None, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    time = models.DateTimeField(default=timezone.now, blank=True)
    measurement_type = models.ForeignKey(MeasurementMaster, on_delete=models.CASCADE, default=None, null=True, blank=True)
    notes = models.CharField(max_length=2000, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='measure_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='measure_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)


    def __str__(self):
        return str(self.id)


class MeasurementPics(models.Model):
    image_name = models.CharField(max_length=400, null=True, blank=True)
    image = models.FileField(upload_to='measure_images', null=True, blank=True)
    images = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='measure_images', default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mpics_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mpics_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name_plural = "MeasurementPics"
		