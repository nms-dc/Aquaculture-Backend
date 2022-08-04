from rest_framework import serializers
from farms.models import Farms, FarmCertification,FarmImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmImage
        fields = '__all__'


#first trying to get nested without image we have foreign key reference in Farms
class CertifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FarmCertification
        fields = '__all__'#["certificate_name","certificate_number","add_information"]


class FarmSerializer(serializers.ModelSerializer):
    certificate = CertifySerializer(many = True)
    #`.create()` method does not support writable nested fields by default- we need to use 'read_only=True'

    class Meta:
        model = Farms
        fields = ["farm_name","farm_area","address_line_one","address_line_two","state","town_village","description",'certificate']
        
    
    def create(self, validated_data):
        
        #image not implemented first trying with certificate
        certificate = validated_data.pop('certificate')
        Farm_instance = Farms.objects.create(**validated_data)
        for data in certificate:
              return data          
        #     FarmCertification.objects.create(certificate=Farm_instance,**data)
        return Farm_instance

