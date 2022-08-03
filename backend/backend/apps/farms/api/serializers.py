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
        fields = ["certificate_name","certificate_number","add_information"]


class FarmSerializer(serializers.ModelSerializer):
    certify = CertifySerializer(many = True)

    class Meta:
        model = Farms
        fields = ["farm_name","farm_area","address_line_one","address_line_two","state","town_village","description",'certify']
        
    
    def create(self, validated_data):
        
        #image not implemented first trying with certificate
        certify = validated_data.pop('certify')
        Farm_instance = Farms.objects.create(**validated_data)
        for data in certify:
            FarmCertification.objects.create(user=Farm_instance,**data)
        return Farm_instance

