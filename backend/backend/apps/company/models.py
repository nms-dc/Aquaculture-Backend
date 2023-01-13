from django.db import models
# from company.models import Company


class Company(models.Model):
    company_name = models.CharField(max_length=200, default='')
    sic_gst_code = models.CharField(max_length=200, default='')
    pan_no = models.CharField(max_length=200, default='')
    address_one = models.TextField(default='')
    address_two = models.TextField(default='')
    pincode = models.IntegerField(default=0)
    website = models.URLField(max_length=200, default='')

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name_plural = "Company"    
