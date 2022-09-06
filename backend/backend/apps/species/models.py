from email.mime import image
from itertools import product
from django.db import models

# Create your models here.
class Species(models.Model):
    
    product_name = models.CharField(max_length=250,null=True)
    product_desc = models.CharField(max_length=250,null=True)
    image = models.FileField(upload_to = 'speciespicture_uploads', null=True)
    fish_common_name = models.CharField(max_length=250,null=True)
    fish_scientific_name = models.CharField(max_length=250,null=True)
    fish_ranges = models.IntegerField(null = True)
    wikipedia = models.CharField(max_length=250,null=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    

class SpeciesCategory(models.Model):
    name = models.CharField(max_length=250,null=True)
    exp = models.IntegerField(null = True)
    parent_category = models.CharField(max_length=250,null=True)
    slug = models.SlugField()
    desc = models.CharField(max_length=250,null=True)
    image_url = models.URLField()
    species_category = models.ForeignKey(Species, on_delete=models.CASCADE, related_name = 'species_category', default = None,null=True)

    