from django.contrib import admin
from farms.models import Farms, FarmImage, FarmCertification
# Register your models here.
admin.site.register(Farms)
admin.site.register(FarmImage)
admin.site.register(FarmCertification)
