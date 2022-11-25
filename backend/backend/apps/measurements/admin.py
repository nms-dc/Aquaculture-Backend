from django.contrib import admin
from measurements.models import Measurement,MeasurementMaster

admin.site.register(Measurement)
admin.site.register(MeasurementMaster)

# Register your models here.
