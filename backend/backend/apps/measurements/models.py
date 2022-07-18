from django.db import models

# Create your models here.

class Measurements(models.Model):
    measurement_max = models.IntegerField(default=0)
    measurement = models.CharField(max_length=24, default = None)
    updatedAt = models.DateField(auto_now= True)
    createdAt = models.DateField(auto_now= True)
    measurement_categories_id = models.IntegerField(default=0)
    measurement_type = models.CharField(max_length=24, default = None)
    measurement_min = models.CharField(max_length=24, default = None)
    #this model goes Foreign Key with MeasurementHistories

    def __str__(self):

        return self.measurement
    

class MeasurementHistories(models.Model):
    createdAt = models.DateField(auto_now= True)
    id = models.IntegerField(default=0)
    updatedAt = models.DateField(auto_now= True)
    categories =  models.CharField(max_length=24, default = None)
    pond_id = models.IntegerField(default=0)
    module = models.CharField(max_length=24, default = None)
    date_measure = models.DateField(auto_now= True)
    measurement_number = models.IntegerField(default=0)
    measurement_id = models.IntegerField(default=0)
    file_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    createdAt = models.DateField(auto_now= True)
    updatedAt = models.DateField(auto_now= True)
    #this module getting foreign key reference from  Measurements
    