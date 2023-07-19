from django.db import models
# from company.models import Company
from accounts.models import User


class CompanyType(models.Model):
    type = models.CharField(max_length=200, default=None, null=True)
    type_description = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return self.type

class CompanyFeedType(models.Model):
    type = models.CharField(max_length=200, default=None, null=True)
    type_description = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return self.type_description


class Company(models.Model):
    choice_company_type=(
                        ('F','feed'),
                        ('P','probiotics'),
                        ('S','seed'),
                        ('F/P','feed/probiotics'))
    
    
    company_name = models.CharField(max_length=200,  blank=True)
    sic_gst_code = models.CharField(max_length=200, default=None, null=True,  blank=True)
    pan_no = models.CharField(max_length=200, default=None, null=True,  blank=True)
    address_one = models.TextField(default=None, null=True,  blank=True)
    address_two = models.TextField(default=None, null=True,  blank=True)
    pincode = models.IntegerField(default=None, null=True,  blank=True)
    website = models.URLField(max_length=200, default=None, null=True,  blank=True)
    company_feed_types = models.ForeignKey(CompanyFeedType, on_delete=models.CASCADE, null=True, blank=True)
    company_types = models.ForeignKey(CompanyType, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=200, default=None, null=True,  blank=True)
    phone = models.CharField(max_length=200, default=None, null=True)
    email = models.EmailField(default=None, null=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_user_create', default=None, null=True)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_user_update', default=None, null=True)
    updated_at = models.DateField(null=True,  blank=True)

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name_plural = "Company"    

