from django.db import models


class Farms(models.Model):

    company_id = models.IntegerField(default=0)
    farm_name = models.CharField(max_length=24, default=None, null=True)
    farm_area = models.IntegerField(default=0, null=True)
    phone = models.IntegerField(default=0, null=True)
    address_line_one = models.TextField(max_length=224, default=None, null=True)
    address_line_two = models.TextField(max_length=224, default=None, null=True)
    city = models.CharField(max_length=24, default=None, null=True)
    country = models.CharField(max_length=24, default=None, null=True)
    town_village = models.CharField(max_length=24, default=None, null=True)
    zipcode = models.IntegerField(default=0, null=True)
    state = models.CharField(max_length=24, default=None, null=True)
    lat = models.IntegerField(default=0, null=True)
    lng = models.IntegerField(default=0, null=True)
    description = models.TextField(max_length=224, default=None, null=True)
    lastupdatedt = models.DateField(auto_now=True, null=True)
    createdAt = models.DateField(auto_now=True, null=True)
    farm_status = models.CharField(max_length=240, default=None, null=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, default=None, null=True)
    district = models.CharField(max_length=24, default=None, null=True)

    def __str__(self):
        return self.farm_name


class FarmImage(models.Model):

    image = models.FileField(upload_to='farmimage_uploads', null=True)
    image_name = models.CharField(max_length=24, default=None, null=True)
    images = models.ForeignKey(Farms, on_delete=models.CASCADE, related_name='farm_images', null=True, blank=True)


class FarmCertification(models.Model):

    certificate_name = models.CharField(max_length=24, default=None, null=True)
    certificate_number = models.IntegerField(default=0, null=True)
    add_information = models.TextField(max_length=224, default=None, null=True)
    image = models.ImageField(upload_to='certificate_uploads', null=True)
    certificates = models.ForeignKey(Farms, on_delete=models.CASCADE, related_name='certificate', null=True, blank=True)
