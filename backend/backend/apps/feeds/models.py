from django.db import models
from cycle.models import Cycle
from django.utils import timezone
from farms.models import FeedLots
from accounts.models import User



class FeedType(models.Model):
    type = models.CharField(max_length=24, default=None, null=True, blank=True)
    type_desc = models.CharField(max_length=24, default=None, null=True, blank=True)
    feed_unit = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self) -> str:
        return str(self.type)

class Feeds(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, default=None, null=True, blank=True)
    feed_type = models.ForeignKey(FeedType, on_delete=models.CASCADE, default=None, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    time = models.DateTimeField(default=timezone.now, blank=True)
    lot = models.ForeignKey(FeedLots, on_delete=models.CASCADE, default=None, null=True, blank=True)
    price_per_kg = models.IntegerField(null=True, blank=True)
    is_probiotic_mixed = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feed_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feed_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id)


class FeedPics(models.Model):
    image_name = models.CharField(max_length=400, null=True, blank=True)
    image = models.FileField(upload_to='feeds_images', null=True, blank=True)
    images = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='feeds_images', default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fpics_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fpics_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name_plural = "Feedpics"