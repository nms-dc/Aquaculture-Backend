from rest_framework import serializers
from farms.models import Farms, FarmCertification,FarmImage
from ponds.models import Ponds
from ponds.api.serializers import PondSummarySerializer
from accounts.models import User

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmImage
        fields = '__all__'


class CertifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FarmCertification
        fields = ["certificate_name","certificate_number","add_information", "image", "certificates"]


class FarmSummarySerializer(serializers.ModelSerializer):
    farm_images = ImageSerializer(many = True)
    
    class Meta:
        model = Farms
        fields = ["id", "farm_name","description","farm_images"]

 
class FarmPondRelationSerializer(serializers.ModelSerializer):
    farm_images = ImageSerializer(many = True)
    ponds = serializers.SerializerMethodField()

    def get_ponds(self,obj):
        try:
            if Ponds.objects.filter(farm=obj).exists():
                ponds = Ponds.objects.filter(farm=obj)
                serializer = PondSummarySerializer(ponds, many=True).data
                return serializer
            else:
                return None
        except Ponds.DoesNotExist:
            return None
        # ponds = PondSummarySerializer(source='*')
    
    class Meta:
        model = Farms
        fields = ["id", "farm_name","description","farm_images","ponds"]


 
class FarmSerializer(serializers.ModelSerializer):
    
    #the variable name exactly should same as related name associated with the foriegn key
    certificate = CertifySerializer(many = True, read_only=True)
    farm_images = ImageSerializer(many = True, read_only=True)
    
    
    class Meta:
        model = Farms
        fields = ["id", "farm_name","farm_area","address_line_one","address_line_two","state","town_village","description", "farm_images","certificate",'user']
  
    
    def create(self, validated_data):
        image_datas = self.context.get('view').request.FILES
        print('image',  image_datas)
        token = self.context.get('request').META.get('HTTP_AQUA_AUTH_TOKEN')
        #user = User.objects.get(email=token)
       
        Farm_instance = Farms.objects.create(
            farm_name = validated_data['farm_name'],
            farm_area = validated_data['farm_area'],
            address_line_one = validated_data['address_line_one'],
            address_line_two = validated_data['address_line_two'],
            state = validated_data['state'],
            town_village = validated_data['town_village'],
            description = validated_data['description'],
            #user = user       
        )

        for image_data in image_datas.getlist('farm_images'):      
             name = image_data.name
             FarmImage.objects.create(images=Farm_instance, image_name=name, image=image_data)

        for certify_data in image_datas.getlist('certificate'):   
             print('certiify', certify_data)   
             name = certify_data.name
             FarmCertification.objects.create(certificates=Farm_instance, certificate_name=name, image=certify_data)
        return Farm_instance


    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        token = self.headers.get('Aqua-Auth-Token', None)
        user = User.objects.get(email=token)
        
        instance.farm_name = validated_data.get('farm_name',instance.farm_name)
        instance.farm_area = validated_data.get('farm_area',instance.farm_area)
        instance.address_line_one = validated_data.get('address_line_one',instance.address_line_one)
        instance.address_line_two = validated_data.get('address_line_two',instance.address_line_two)
        instance.state = validated_data.get('state',instance.state)
        instance.town_village = validated_data.get('town_village',instance.town_village)
        instance.description = validated_data.get('description',instance.description)
        instance.user = user
        instance.save()
        
        certify_with_same_profile_instance = FarmCertification.objects.filter(certificates=instance.pk).values_list('id', flat=True)
        image_with_same_profile_instance = FarmImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        for certify_id in certify_with_same_profile_instance:
            FarmCertification.objects.filter(pk = certify_id).delete()

        for image_id in image_with_same_profile_instance:
            FarmImage.objects.filter(pk = image_id).delete()           

        for certify_data in image_datas.getlist('certificate'):      
             name = certify_data.name
             FarmCertification.objects.create(certificates=instance, certificate_name=name, image=certify_data)

        for image_data in image_datas.getlist('farm_images'):      
             name = image_data.name
             FarmImage.objects.create(images=instance, image_name=name, image=image_data)

        return instance      