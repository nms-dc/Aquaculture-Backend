from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=200, default='')
    sic_gst_code = models.CharField(max_length=200, default='')
    pan_no = models.CharField(max_length=200, default='')
    address_one = models.TextField(default='')
    address_two = models.TextField(default='')

