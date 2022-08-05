from rest_framework import serializers

from ponds.models import Ponds,PondType, PondConstructType,PondImage

class PondTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondType
        fields = '__all__'

class PondConstructTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PondConstructType
        fields = '__all__'

class PondImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PondImage
        fields = '__all__'        

class PondSummarySerializer(serializers.ModelSerializer):
    pond_types = PondTypeSerializer(many=True)
    PondConstructTypes = PondConstructTypeSerializer(many=True)
    pond_images = PondImageSerializer(many=True)

    class Meta:
        model = Ponds
        fields = ['id','pond_types','PondConstructTypes','pond_images']


class PondSerializer(serializers.ModelSerializer):

    pond_types = PondTypeSerializer(many=True)
    PondConstructTypes = PondConstructTypeSerializer(many=True)
    pond_images = PondImageSerializer(many=True)

    class Meta:
        model = Ponds
        fields = ['id','PondConstructTypes','pond_images','pond_name','pond_length','pond_breadth','pond_depth','pond_area','pond_capacity','description','pond_types']
    
    def create(self, validated_data):
        
        pond_type = validated_data.pop('pond_types')
        pond_construct = validated_data.pop('PondConstructTypes')
        pond_image = validated_data.pop('pond_images')# here we have to pass related name we have defined in our models like in
        #this line 'pond_images'
        pond_instance = Ponds.objects.create(**validated_data)

        for data in pond_type:                      
            PondType.objects.create(pond_type=pond_instance,**data)

        for data in pond_construct:                      
            PondConstructType.objects.create(Pond_ConstructTypes=pond_instance,**data)

        for data in pond_image:                      
            PondImage.objects.create(images=pond_instance,**data)
            #we have to mention the field that defined in model for example 'images' in the above line
            
        return pond_instance

    def update(self, instance, validated_data):

        pond_type = validated_data.pop('pond_types')
        pond_construct = validated_data.pop('PondConstructTypes')
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
        pondtype_with_same_profile_instance = PondType.objects.filter(pond_type=instance.pk).values_list('id', flat=True)
        construct_with_same_profile_instance = PondConstructType.objects.filter(Pond_ConstructTypes=instance.pk).values_list('id', flat=True)
        pondimage_with_same_profile_instance = PondImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        for pondtype_id in pondtype_with_same_profile_instance:
            PondType.objects.filter(pk = pondtype_id).delete()

        for construct_id in construct_with_same_profile_instance:
            PondConstructType.objects.filter(pk = construct_id).delete()

        for pondimage_id in pondimage_with_same_profile_instance:
            PondImage.objects.filter(pk = pondimage_id).delete()        

        for data in pond_type:
            pondtype_instance = PondType.objects.create(pond_type = instance,**data)
            pondtype_instance.name = data['name']
            pondtype_instance.desc = data['desc']
            pondtype_instance.save()

        for data in pond_construct:
            construct_instance = PondConstructType.objects.create(Pond_ConstructTypes = instance, **data)
            construct_instance.construct_type = data['construct_type']
            construct_instance.save()

        for data in pond_image:
            pondimage_instance = PondImage.objects.create(images = instance, **data)
            pondimage_instance.image = data['image']
            pondimage_instance.user = data['user']
            pondimage_instance.save()            

        return instance    