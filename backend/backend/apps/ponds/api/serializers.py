from rest_framework import serializers

from ponds.models import Ponds

class PondSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ponds
        #location field is not available but FE guys need it
        fields = ['pond_type','pond_construct_type','pond_name','pond_length','pond_breadth','pond_depth','pond_area','pond_capacity','description','image']