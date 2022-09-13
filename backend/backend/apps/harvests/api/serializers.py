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

class HarvestPondImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HarvestPondImages
        fields = '__all__'  

class LogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HarvestLogisticImages
        fields = '__all__'  


# class AddAnimalSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = AddAnimal
#         fields = '__all__'  
        
class  HarvestSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Harvests
        fields = ['harvest_type','harvest_date','harvest_notes']        
        
        
class HarvestSerializer(serializers.ModelSerializer):

    ani_images = AnimalImageSerializer(many=True, read_only=True)
    pond_images = HarvestPondImageSerializer(many=True, read_only=True)
    log_images = LogImageSerializer(many=True,read_only=True)

    class Meta:
        model = Harvests
        fields = '__all__'
        
    
    def create(self, validated_data):
        #the below fields for image upload and extract the names from the image
        image_data = self.context.get('view').request.FILES
        harvest_instance = Harvests.objects.create(
        harvest_type = validated_data['harvest_type'],
        total_kgs = validated_data['total_kgs'],
        temperature = validated_data['temperature'],
        sold_to = validated_data['sold_to'],
        harvest_notes = validated_data['harvest_notes'],
        harvest_cost = validated_data['harvest_cost'],
        cycle = validated_data['cycle'],
        animal_count_1 = validated_data['animal_count_1'],
        total_kg_1 = validated_data['total_kg_1'],
        price_kg_1 = validated_data['price_kg_1'],
        is_chill_kill = validated_data['is_chill_kill']           
        )


        #below the three loops helps us to upload image and extracts names from that
        for data in image_data.getlist('ani_images'): 
            name = data.name                      
            HarvestAnimalImages.objects.create(images=harvest_instance, image_name=name, image=data)
            
        for data in image_data.getlist('pond_images'): 
            name = data.name                      
            HarvestPondImages.objects.create(images=harvest_instance, image_name=name, image=data)    
        
        for data in image_data.getlist('log_images'): 
            name = data.name                      
            HarvestLogisticImages.objects.create(images=harvest_instance, image_name=name, image=data)
        
        #this for loop used to store the value of AddAnimal Model related with 'FK' with main Harvest model   
        # for image in image_data:
        #     AddAnimal.objects.create(adding_animal=harvest_instance,**image)
            
        return harvest_instance
    
    
    
    
    #this update method only works for images not for 'AddAnimals'
    def update(self, instance, validated_data):
        image_data = self.context.get('view').request.FILES
        # ani_image = self.context.get('view').request.FILES
        # pond_image = self.context.get('view').request.FILES
        # log_image = self.context.get('view').request.FILES
        instance.harvest_type = validated_data.get('harvest_type',instance.harvest_type)
        instance.total_kgs = validated_data.get('total_kgs',instance.total_kgs)
        instance.temperature = validated_data.get('temperature',instance.temperature)       
        instance.sold_to = validated_data.get('sold_to',instance.sold_to)
        instance.harvest_notes = validated_data.get('harvest_notes',instance.harvest_notes)
        instance.harvest_cost = validated_data.get('harvest_cost',instance.harvest_cost)
        instance.cycle = validated_data.get('cycle',instance.cycle)
        instance.animal_count_1 = validated_data('animal_count_1',instance.animal_count_1)
        instance.total_kg_1 = validated_data('total_kg_1',instance.total_kg_1)
        instance.price_kg_1 = validated_data('price_kg_1',instance.price_kg_1)
        instance.is_chill_kill = validated_data('is_chill_kill',instance.is_chill_kill)
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

        for data in image_data.getlist('pond_images'): 
            name = data.name                      
            HarvestPondImages.objects.create(images=instance, image_name=name, image=data)         


        for data in image_data.getlist('ani_images'): 
            name = data.name                      
            HarvestAnimalImages.objects.create(images=instance, image_name=name, image=data) 
        
        for data in image_data.getlist('log_images'): 
            name = data.name                      
            HarvestLogisticImages.objects.create(images=instance, image_name=name, image=data)            

        
        return instance 
        