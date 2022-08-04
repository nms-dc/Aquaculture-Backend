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
    
    #the variable name exactly should same as related name associated with the foriegn key
    certificate = CertifySerializer(many = True)
    image = ImageSerializer(many = True)
    #we need to use 'read_only=True',for represent json without using create because --
    #create method will  not support writable nested fields by default.we have to write a function

    
    class Meta:
        model = Farms
        fields = ["farm_name","farm_area","address_line_one","address_line_two","state","town_village","description",'certificate','image']
        
    
    def create(self, validated_data):
        
        #image not implemented first trying with certificate
        certify_datas = validated_data.pop('certificate')
        Farm_instance = Farms.objects.create(**validated_data)
        for data in certify_datas:
                     
             FarmCertification.objects.create(certificates=Farm_instance,**data)
        return Farm_instance

