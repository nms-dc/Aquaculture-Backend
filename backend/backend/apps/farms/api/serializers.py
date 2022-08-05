from rest_framework import serializers
from farms.models import Farms, FarmCertification,FarmImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmImage
        fields = '__all__'


class CertifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FarmCertification
        fields = '__all__'#["certificate_name","certificate_number","add_information"]


class FarmSummarySerializer(serializers.ModelSerializer):
    farm_images = ImageSerializer(many = True)
    
    class Meta:
        model = Farms
        fields = ["id", "farm_name","description","farm_images"]
 
 
class FarmSerializer(serializers.ModelSerializer):
    
    #the variable name exactly should same as related name associated with the foriegn key
    certificate = CertifySerializer(many = True)
    farm_images = ImageSerializer(many = True)
    
    class Meta:
        model = Farms
        fields = ["id", "farm_name","farm_area","address_line_one","address_line_two","state","town_village","description","certificate", "farm_images"]
  
    
    def create(self, validated_data):
        certify_datas = validated_data.pop('certificate')
        image_datas = validated_data.pop('farm_images')  
        Farm_instance = Farms.objects.create(**validated_data)
        for data in certify_datas:                   
             FarmCertification.objects.create(certificates=Farm_instance,**data)
        for image_data in image_datas:                   
             FarmImage.objects.create(images=Farm_instance,**image_data)
        return Farm_instance


    def update(self, instance, validated_data):
        certify_datas = validated_data.pop('certificate')
        image_datas = validated_data.pop('farm_images')  
        instance.farm_name = validated_data.get('farm_name',instance.farm_name)
        instance.farm_area = validated_data.get('farm_area',instance.farm_area)
        instance.address_line_one = validated_data.get('address_line_one',instance.address_line_one)
        instance.address_line_two = validated_data.get('address_line_two',instance.address_line_two)
        instance.state = validated_data.get('state',instance.state)
        instance.town_village = validated_data.get('town_village',instance.town_village)
        instance.description = validated_data.get('description',instance.description)
        instance.save()
        
        certify_with_same_profile_instance = FarmCertification.objects.filter(certificates=instance.pk).values_list('id', flat=True)
        image_with_same_profile_instance = FarmImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        for certify_id in certify_with_same_profile_instance:
            FarmCertification.objects.filter(pk = certify_id).delete()

        for image_id in image_with_same_profile_instance:
            FarmImage.objects.filter(pk = image_id).delete()           

        for data in certify_datas:
            Certify_instance = FarmCertification.objects.create(certificates = instance,**data)
            Certify_instance.certificate_name = data['certificate_name']
            Certify_instance.certificate_number = data['certificate_number']
            Certify_instance.add_information = data['add_information']
            Certify_instance.image = data['image']
            Certify_instance.save()

        for data in image_datas:
            image_instance = FarmImage.objects.create(images = instance, **data)
            image_instance.image = data['image']
            image_instance.image_name = data['image_name']
            image_instance.save()

        return instance           