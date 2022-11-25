from django.contrib import admin
from measurements.models import Measurement,MeasurementType

admin.site.register(Measurement)
admin.site.register(MeasurementType)

# Register your models here.
