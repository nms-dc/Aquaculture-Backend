from django.db import models

# Create your models here.
class Countries(models.Model):

    alpha_2_code = models.IntegerField(default=0)
    alpha_3_code = models.IntegerField(default=0)
    createdAt = models.OneToOneField('accounts.Currencies',on_delete=models.CASCADE)# both side declared as one
    updatedAt = models.DateField(auto_now= True)
    country_name = models.CharField(max_length=24, default = None)
    #this models has foreign Key reference from state  model but dont know where it comes
    #this models has one to one reference from Farms  model but dont know where it comes
    #this models has one to one reference from country_codes_phone  model but dont know where it comes
    #this models has one  to one reference from User  model but dont know where it comes


    def __str__(self):

        return self.country_name


class State(models.Model):

    updatedAt = models.DateField(auto_now= True)
    state = models.CharField(max_length=24, default = None)
    vehicle_code = models.IntegerField(default=0)
    country_id = models.IntegerField(default=0)
    createdAt = models.DateField(auto_now= True)

    def __str__(self):

        return self.state

class CountryCodesPhone(models.Model):

    country_id = models.IntegerField(default=0)
    updatedAt = models.DateField(auto_now= True)
    createdAt = models.DateField(auto_now= True)
    country_phone_code = models.IntegerField(default=0)

    #this model has one to one relationship with Countries dont know where it comes


class Tiers(models.Model):

    updatedAt = models.DateField(auto_now= True)
    createdAt = models.DateField(auto_now= True)
    json_features = models.CharField(max_length=24, default = None)
    html_text = models.CharField(max_length=24, default = None)
    cost = models.IntegerField(default=0)
    tier = models.CharField(max_length=24, default = None)

    def __str__(self):

        return self.tier

     