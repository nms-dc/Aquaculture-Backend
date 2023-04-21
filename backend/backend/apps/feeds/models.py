from django.db import models
from cycle.models import Cycle
from django.utils import timezone
from farms.models import FeedLots
from accounts.models import User



class FeedType(models.Model):
    type = models.CharField(max_length=24, default=None, null=True)
    type_desc = models.CharField(max_length=24, default=None, null=True)
    feed_unit = models.CharField(max_length=100, blank=True, null=True)
    

class Feeds(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, default=None, null=True)
    feed_type = models.ForeignKey(FeedType, on_delete=models.CASCADE, default=None, null=True)
    value = models.FloatField(null=True)
    time = models.DateTimeField(default=timezone.now)
    lot = models.ForeignKey(FeedLots, on_delete=models.CASCADE, default=None, null=True)
    price_per_kg = models.IntegerField(null=True)
    is_probiotic_mixed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feed_user_create', default=None, null=True)
    created_at = models.DateField(auto_now=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feed_user_update', default=None, null=True)
    updated_at = models.DateField(auto_now=True, null=True)