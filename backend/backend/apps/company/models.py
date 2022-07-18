from django.db import models

# Create your models here.
class CompanyType(models.Model):
    company_type = models.CharField(max_length=24, default = None)

    def __str__(self):

        return self.company_type

class Companies(models.Model):

    address_line_2 = models.TextField(max_length=224, default = None)
    city = models.CharField(max_length=24, default = None)
    state_id = models.IntegerField(default=0)
    country_id = models.ForeignKey('common.Countries',on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    company_website = models.URLField(help_text = 'type the company website')
    address_line_1 = models.TextField(max_length=224, default = None)
    company_name = models.CharField(max_length=24, default = None)
    tier_id = models.ForeignKey('common.Tiers', on_delete=models.CASCADE)
    company_type_id = models.OneToOneField(CompanyType,on_delete=models.CASCADE)
    default_currency_id = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    media_code_id = models.IntegerField(default=0)
    is_registered = models.BooleanField(default = True)
    public_id = models.IntegerField(default=0)
    qr_code_path = models.TextField(max_length=224, default = None)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    pictures = models.ImageField(upload_to = None, height_field = None, width_field = None)
    createdAt = models.DateField(auto_now= True)
    updatedAt = models.DateField(auto_now= True)
    createdAt_id = models.IntegerField(default=0)
    updatedAt_id = models.IntegerField(default=0)

    #this model has FK reference from User model dont know the field


    def __str__(self):

        return self.company_name
