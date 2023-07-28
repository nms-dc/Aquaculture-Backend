import datetime
from django.db import models
from farms.models import Farms
from accounts.models import User


class PondConstructType(models.Model):
    construct_type = models.CharField(max_length=24, default=None, null=True, blank=True)
    def __str__(self):
        return self.construct_type

class PondType(models.Model):
    name = models.CharField(max_length=24, default=None, blank=True)
    desc = models.CharField(max_length=24, default=None, blank=True)
    pond_construct = models.ForeignKey(PondConstructType, on_delete=models.CASCADE, related_name='Pond_construct', null=True, blank=True)

    def __str__(self):
        return self.name

class Ponds(models.Model):
    pond_name = models.CharField(max_length=240, default=None, blank=True)
    pond_length = models.FloatField(null=True, blank=True)
    pond_depth = models.FloatField(null=True, blank=True)
    pond_breadth = models.FloatField(null=True, blank=True)
    pond_area = models.FloatField(null=True, blank=True)
    pond_capacity = models.FloatField(null=True, blank=True)
    pond_type = models.ForeignKey(PondType, on_delete=models.CASCADE, related_name='pond_types', null=True, blank=True)
    pond_construct_type = models.ForeignKey(PondConstructType, on_delete=models.CASCADE, related_name='pond_construct_types', null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    location = models.TextField(max_length=2024, default=None, null=True, blank=True)
    description = models.CharField(max_length=240, default=None, blank=True)
    createdAt = models.DateField(auto_now=True, null=True, blank=True)
    lastupdatedt = models.DateField(auto_now=True, null=True, blank=True)
    pond_number = models.IntegerField(default=0,  null=True, blank=True)
    last_feed_datetime = models.DateField(auto_now=True, null=True, blank=True)
    last_preparation_time = models.DateField(auto_now=True, null=True, blank=True)
    last_stock_date = models.DateField(auto_now=True, null=True, blank=True)
    estimated_harvest_date = models.DateField(auto_now=True, null=True, blank=True)
    farm = models.ForeignKey('farms.Farms', on_delete=models.CASCADE, default=None, null=True, blank=True)
    is_active_pond = models.BooleanField(default=False, blank=True)
    active_cycle_id = models.IntegerField(null=True, blank=True)
    active_cycle_date = models.DateField(null=True, blank=True)
    no_of_harvests = models.IntegerField(default=0, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pond_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pond_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.pond_name
    
    class Meta:
        verbose_name_plural = "Ponds"


    @property
    def doc(self):
        if self.active_cycle_date is None:
            return 0
        else:
            delta = datetime.date.today() - self.active_cycle_date
            return delta.days


class PondImage(models.Model):
    image = models.FileField(upload_to='pond_images', null=True, blank=True)
    image_name = models.CharField(max_length=24, default=None, null=True, blank=True)
    images = models.ForeignKey(Ponds, on_delete=models.CASCADE, related_name='pond_images', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pimage_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pimage_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.image_name)


def get_default_info():
    return {'measurement_id': None}


class PondGraphs(models.Model):
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, related_name='grphs_of_a_farm', blank=True)
    pond = models.ForeignKey(Ponds, on_delete=models.CASCADE, related_name='graphs_of_pond', null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    abw = models.FloatField(null=True, blank=True)
    total_feed = models.FloatField(null=True, blank=True)
    extra_info = models.JSONField(null=True, blank=True, default=get_default_info)
    cycle = models.ForeignKey('cycle.Cycle', on_delete=models.CASCADE, null=True, related_name='cycle_id', blank=True)

    def __str__(self):
        return "pond_graphs_id"+str(self.id)

    class Meta:
        verbose_name_plural = "PondGraphs"


class PondAnalytics(models.Model):
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, null=True, related_name='pond_farm_analytics', blank=True)
    pond = models.ForeignKey(Ponds, on_delete=models.CASCADE, related_name='pond_analytics', null=True, blank=True)
    no_of_cycles = models.IntegerField(default=0,  null=True, blank=True)
    harvest_amount = models.FloatField(null=True, blank=True)
    total_feed = models.FloatField(null=True, blank=True)
    extra_info = models.JSONField(null=True, blank=True, default=get_default_info)

    def __str__(self):
        return "pond_analytics_id:"+str(self.id)

    class Meta:
        verbose_name_plural = "PondAnalytics"
