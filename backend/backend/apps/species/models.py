from django.db import models

# Create your models here.
class SpeciesImage(models.Model):

    image = models.ImageField(upload_to = 'uploads', height_field = None, width_field = None)
    user = models.CharField(max_length=24, default = None)

class SpeciesCategory(models.Model):

    name = models.CharField(max_length=24, default = None)
    exp = models.FloatField(null=True)
    parent_category = models.CharField(max_length=24, default = None)
    slug = models.SlugField(max_length=200)
    desc = models.TextField(max_length=224, default = None)
    image_url = models.URLField(max_length=200)


class Species(models.Model):

    product_name = models.CharField(max_length=24, default = None)
    product_desc = models.TextField(max_length=224, default = None)
    image = models.ForeignKey(SpeciesImage, on_delete=models.CASCADE)
    species_category = models.ForeignKey(SpeciesCategory, on_delete=models.CASCADE) 
    #if the FK model in the same file we dont have to use quotes        
    fist_common_name = models.CharField(max_length=24, default = None)
    fish_scientific_name = models.CharField(max_length=24, default = None)
    fish_ranges = models.IntegerField(default=0)
    wikipedia = models.TextField(max_length=224, default = None)
    createdAt = models.DateField(auto_now= True)
    updatedAt = models.DateField(auto_now= True)

    def __str__(self):

        return self.product_name

    