from email.mime import image
from itertools import product
from django.db import models
from accounts.models import User


class SpeciesCategory(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    exp = models.IntegerField(null=True, blank=True)
    parent_category = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField( null=True, blank=True)
    desc = models.CharField(max_length=250, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return str(self.name)

# Create your models here.
class Species(models.Model):

    product_name = models.CharField(max_length=250, null=True, blank=True)
    product_desc = models.CharField(max_length=250, null=True, blank=True)
    image = models.FileField(upload_to='speciespicture_uploads', null=True, blank=True)
    fish_common_name = models.CharField(max_length=250, null=True, blank=True)
    fish_scientific_name = models.CharField(max_length=250, null=True, blank=True)
    fish_ranges = models.IntegerField(null=True, blank=True)
    wikipedia = models.CharField(max_length=250, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='species_user_create', default=None, null=True, blank=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='species_user_update', default=None, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    species_category = models.ForeignKey(SpeciesCategory, on_delete=models.CASCADE, related_name='species_category', default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id)






