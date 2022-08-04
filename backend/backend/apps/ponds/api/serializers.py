from rest_framework import serializers

from ponds.models import Ponds,PondType

class PondTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondType
        fields = '__all__'


class PondSerializer(serializers.ModelSerializer):

    pond_types = PondTypeSerializer(many=True)
    class Meta:
        model = Ponds
        
        fields = ['pond_construct_type','pond_name','pond_length','pond_breadth','pond_depth','pond_area','pond_capacity','description','image','pond_types']
    
    def create(self, validated_data):
        
        pond_type = validated_data.pop('pond_types')
        pond_instance = Ponds.objects.create(**validated_data)
        for data in pond_type:
                        
            PondType.objects.create(pond_type=pond_instance,**data)
        return pond_instance
