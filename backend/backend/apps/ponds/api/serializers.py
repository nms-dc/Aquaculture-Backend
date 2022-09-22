from rest_framework import serializers
from ponds.models import Ponds,PondImage
from accounts.models import User

class PondImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PondImage
        fields = '__all__'  


class PondSummarySerializer(serializers.ModelSerializer):
    pond_images = PondImageSerializer(many = True)
    doc = serializers.Field(source='doc')
    
    class Meta:
        model = Ponds
        fields = ["id", "pond_name","description","pond_images", "pond_type", "is_active_pond", "doc"]

class PondsSerializer(serializers.ModelSerializer):

    pond_images = PondImageSerializer(many=True, read_only=True)
    # doc = serializers.Field(source='doc')


    class Meta:
        model = Ponds
        fields = ['id','pond_images','pond_name','pond_length','pond_breadth','pond_depth','pond_area','pond_capacity','description','pond_type','pond_construct_type', 'is_active_pond', 'active_cycle_id','farm', 'doc']

    def create(self, validated_data):
        pond_image = self.context.get('view').request.FILES
        # token = self.context.get('request').META.get('HTTP_AQUA_AUTH_TOKEN')
        # #user = User.objects.get(email=token)
        pond_instance = Ponds.objects.create(
        pond_name = validated_data['pond_name'],
        pond_type = validated_data['pond_type'],
        pond_construct_type = validated_data['pond_construct_type'],
        pond_length = validated_data['pond_length'],
        pond_breadth = validated_data['pond_breadth'],
        pond_depth = validated_data['pond_depth'],
        pond_area = validated_data['pond_area'],
        pond_capacity = validated_data['pond_capacity'],
        description = validated_data['description'],
        farm = validated_data['farm']      
        )

        for data in pond_image.getlist('pond_images'): 
            name = data.name                      
            PondImage.objects.create(images=pond_instance, image_name=name, image=data)
        return pond_instance
        
    def update(self, instance, validated_data):

        pond_image = self.context.get('view').request.FILES
        instance.pond_name = validated_data.get('pond_name',instance.pond_name)
        instance.pond_type = validated_data.get('pond_type',instance.pond_type)
        instance.pond_construct_type = validated_data.get('pond_construct_type',instance.pond_construct_type)       
        instance.pond_length = validated_data.get('pond_length',instance.pond_length)
        instance.pond_breadth = validated_data.get('pond_breadth',instance.pond_breadth)
        instance.pond_depth = validated_data.get('pond_depth',instance.pond_depth)
        instance.pond_area = validated_data.get('pond_area',instance.pond_area)
        instance.pond_capacity = validated_data.get('pond_capacity',instance.pond_capacity)
        instance.description = validated_data.get('description',instance.description)
        instance.farm = validated_data.get('farm',instance.farm)
        instance.save()

        #here also we have to reference models fields only like 'pond_type=instance.pk'
        pondimage_with_same_profile_instance = PondImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        for pondimage_id in pondimage_with_same_profile_instance:
            PondImage.objects.filter(pk = pondimage_id).delete()        

        for data in pond_image.getlist('pond_images'): 
            name = data.name                      
            PondImage.objects.create(images=instance, image_name=name, image=data)         

        return instance          

