from rest_framework import serializers
from farms.models import Farms

class farmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farms
        fields = ['farm_name','farm_area','address_line_one','address_line_two','state','town_village','description','image','certificate']