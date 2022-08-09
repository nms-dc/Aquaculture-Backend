from rest_framework import serializers
from ponds.models import Ponds,PondImage

class PondImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PondImage
        fields = '__all__'  


class PondSummarySerializer(serializers.ModelSerializer):
    pond_images = PondImageSerializer(many = True)
    
    class Meta:
        model = Ponds
        fields = ["id", "pond_name","description","pond_images"]

class PondsSerializer(serializers.ModelSerializer):

    pond_images = PondImageSerializer(many=True)

    class Meta:
        model = Ponds
        fields = ['id','pond_images','pond_name','pond_length','pond_breadth','pond_depth','pond_area','pond_capacity','description','pond_type','pond_construct_type']

    def create(self, validated_data):
        
        pond_image = validated_data.pop('pond_images')# here we have to pass related name we have defined in our models like in
        #this line 'pond_images'
        pond_instance = Ponds.objects.create(**validated_data)

        for data in pond_image:                      
            PondImage.objects.create(images=pond_instance,**data)
            #we have to mention the field 'related_name' that defined in model for example 'images' in the above line
            
        return pond_instance
    def update(self, instance, validated_data):

        pond_image = validated_data.pop('pond_images')

        #here we have to reference normal fields not FK fields from main model(here- Ponds)
        instance.pond_name = validated_data.get('pond_name',instance.pond_name)
        instance.pond_length = validated_data.get('pond_length',instance.pond_length)
        instance.pond_breadth = validated_data.get('pond_breadth',instance.pond_breadth)
        instance.pond_depth = validated_data.get('pond_depth',instance.pond_depth)
        instance.pond_area = validated_data.get('pond_area',instance.pond_area)
        instance.pond_capacity = validated_data.get('pond_capacity',instance.pond_capacity)
        instance.description = validated_data.get('description',instance.description)
        instance.save()

        #here also we have to reference models fields only like 'pond_type=instance.pk'
        pondimage_with_same_profile_instance = PondImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        for pondimage_id in pondimage_with_same_profile_instance:
            PondImage.objects.filter(pk = pondimage_id).delete()        

        for data in pond_image:
            pondimage_instance = PondImage.objects.create(images = instance, **data)
            pondimage_instance.image = data['image']
            pondimage_instance.user = data['user']
            pondimage_instance.save()            

        return instance          