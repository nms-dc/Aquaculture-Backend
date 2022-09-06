from itertools import count
from rest_framework import serializers
from cycle.models import Cycle, CyclePondImage, CycleSeedImage
from accounts.models import User
from harvests.models import Harvests,AddAnimal,HarvestAnimalImages,HarvestLogisticImages,HarvestPondImages

from ponds.models import Ponds

class AnimalImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HarvestAnimalImages
        fields = '__all__'  

class PondImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HarvestPondImages
        fields = '__all__'  

class LogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HarvestLogisticImages
        fields = '__all__'  


class AddAnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddAnimal
        fields = '__all__'  
        
class  HarvestSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Harvests
        fields = ['pond_type','harvest_date','harvest_notes']        
        
        
class HarvestSerializer(serializers.ModelSerializer):

    animal_images = AddAnimalSerializer(many=True)
    ani_images = AnimalImageSerializer(many=True, read_only=True)
    pond_images = PondImageSerializer(many=True, read_only=True)
    log_images = LogImageSerializer(many=True,read_only=True)

    class Meta:
        model = Harvests
        fields = '__all__'
        
    
    def create(self, validated_data):
        #this field for nested data validating we have pop the data first
        image_data = validated_data.pop('animal_images')
        #the below fields for image upload and extract the names from the image
        ani_image = self.context.get('view').request.FILES
        pond_image = self.context.get('view').request.FILES
        log_image = self.context.get('view').request.FILES
        token = self.context.get('request').META.get('HTTP_AQUA_AUTH_TOKEN')
        #user = User.objects.get(email=token)
        harvest_instance = Harvests.objects.create(
        pond_type = validated_data['pond_type'],
        total_kgs = validated_data['total_kgs'],
        temperature = validated_data['temperature'],
        sold_to = validated_data['sold_to'],
        harvest_notes = validated_data['harvest_notes'],
        harvest_cost = validated_data['harvest_cost'],
        cycle = validated_data['cycle'],
            
        )


        #below the three loops helps us to upload image and extracts names from that
        for data in ani_image.getlist('ani_images'): 
            name = data.name                      
            HarvestAnimalImages.objects.create(images=harvest_instance, image_name=name, image=data)
            
        for data in pond_image.getlist('pond_images'): 
            name = data.name                      
            HarvestPondImages.objects.create(images=harvest_instance, image_name=name, image=data)    
        
        for data in log_image.getlist('log_images'): 
            name = data.name                      
            HarvestLogisticImages.objects.create(images=harvest_instance, image_name=name, image=data)
        
        #this for loop used to store the value of AddAnimal Model related with 'FK' with main Harvest model   
        for image in image_data:
            AddAnimal.objects.create(adding_animal=harvest_instance,**image)
            
        return harvest_instance
    
    
    
    
    #this update method only works for images not for 'AddAnimals'
    def update(self, instance, validated_data):
        images_list = self.context.get('view').request.FILES
        # ani_image = self.context.get('view').request.FILES
        # pond_image = self.context.get('view').request.FILES
        # log_image = self.context.get('view').request.FILES
        instance.pond_type = validated_data.get('pond_type',instance.pond_type)
        instance.total_kgs = validated_data.get('total_kgs',instance.total_kgs)
        instance.temperature = validated_data.get('temperature',instance.temperature)       
        instance.sold_to = validated_data.get('sold_to',instance.sold_to)
        instance.harvest_notes = validated_data.get('harvest_notes',instance.harvest_notes)
        instance.harvest_cost = validated_data.get('harvest_cost',instance.harvest_cost)
        instance.cycle = validated_data.get('cycle',instance.cycle)
        instance.save()

        #here also we have to reference models fields only like 'pond_type=instance.pk'
        pondimage_with_same_profile_instance = HarvestPondImages.objects.filter(images=instance.pk).values_list('id', flat=True)
        ani_image_with_same_profile_instance = HarvestAnimalImages.objects.filter(images=instance.pk).values_list('id', flat=True)
        log_image_with_same_profile_instance = HarvestLogisticImages.objects.filter(images=instance.pk).values_list('id', flat=True)


        for pondimage_id in pondimage_with_same_profile_instance:
            HarvestPondImages.objects.filter(pk = pondimage_id).delete()        

        for seedimage_id in ani_image_with_same_profile_instance:
            HarvestAnimalImages.objects.filter(pk = seedimage_id).delete() 
            
        for seedimage_id in log_image_with_same_profile_instance:
            HarvestLogisticImages.objects.filter(pk = seedimage_id).delete()            

        for data in images_list.getlist('pond_images'): 
            name = data.name                      
            HarvestPondImages.objects.create(images=instance, image_name=name, image=data)         


        for data in images_list.getlist('ani_images'): 
            name = data.name                      
            HarvestAnimalImages.objects.create(images=instance, image_name=name, image=data) 
        
        for data in images_list.getlist('log_images'): 
            name = data.name                      
            HarvestLogisticImages.objects.create(images=instance, image_name=name, image=data)            

        
        for data in images_list.getlist('animal_images'): 
                       
            AddAnimal.objects.create(adding_animal=instance,**data)            



        return instance 
        
