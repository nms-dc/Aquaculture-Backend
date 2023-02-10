from django.db import models
# from company.models import Company


class Company(models.Model):
    choice_company_type=(
                        ('F','feed'),
                        ('P','probiotics'),
                        ('S','seed'),
                        ('F/P','feed/probiotics'))
    
    
    company_name = models.CharField(max_length=200)
    sic_gst_code = models.CharField(max_length=200, default=None, null=True)
    pan_no = models.CharField(max_length=200, default=None, null=True)
    address_one = models.TextField(default=None, null=True)
    address_two = models.TextField(default=None, null=True)
    pincode = models.IntegerField(default=None, null=True)
    website = models.URLField(max_length=200, default=None, null=True)
    company_type = models.CharField(max_length=200, choices= choice_company_type, default='F')
    

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name_plural = "Company"    


class CompanyFeedType(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True )
    feed_type = models.CharField(max_length=256, default=None, null=True)

