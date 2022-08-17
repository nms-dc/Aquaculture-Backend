from django.contrib import admin
from ponds.models import Ponds, PondType, PondConstructType, PondImage
# Register your models here.
admin.site.register(PondType)
admin.site.register(PondConstructType)
admin.site.register(Ponds)
admin.site.register(PondImage)
