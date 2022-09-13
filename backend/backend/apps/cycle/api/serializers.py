from rest_framework import serializers
from cycle.models import Cycle, CyclePondImage, CycleSeedImage
from accounts.models import User
from harvests.models import Harvests
from harvests.api.serializers import HarvestSummarySerializer

from ponds.models import Ponds



class PondImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CyclePondImage
        fields = '__all__'  
        
class SeedImageSerializer(serializers.ModelSerializer):        
    
    class Meta:
        model = CycleSeedImage    
        fields = '__all__'


class CycleHarvestRelationSerializer(serializers.ModelSerializer):
    #if we use SerializerMethodField() -- to a variable here in our case ponds by default it will look the function
    #called 'get_ponds' so that reason only we are giving the method 'get_ponds'
    harvest = serializers.SerializerMethodField()

    def get_harvest(self,obj):
        try:
            if Harvests.objects.filter(cycles=obj).exists():
                harvests = Harvests.objects.filter(cycles=obj)
                serializer = HarvestSummarySerializer(harvests, many=True).data
                return serializer
            else:
                return None
        except Ponds.DoesNotExist:
            return None
        
    
    class Meta:
        model = Cycle
        fields = ["id", "species","description","species_pl_stage","harvest"]  

      
class CycleSerializer(serializers.ModelSerializer):

    pond_images = PondImageSerializer(many=True,read_only=True)
    seed_images= SeedImageSerializer(many=True,read_only=True)
    

    class Meta:
        model = Cycle
        fields = ['id','Pond','species','speciesPlStage','seed_company','invest_amount','pondPrep_cost',
        'description','lastupdatedt','seeding_date','pond_images','seed_images', 'numbers_of_larva']

    def create(self, validated_data):
            
            pond_image = self.context.get('view').request.FILES
            seed_image = self.context.get('view').request.FILES
            cycle_instance = Cycle.objects.create(
            species = validated_data['species'],
            speciesPlStage = validated_data['speciesPlStage'],
            invest_amount = validated_data['invest_amount'],
            pondPrep_cost = validated_data['pondPrep_cost'],
            description = validated_data['description'],
            Pond = validated_data['Pond'],
            seed_company = validated_data['seed_company'],
            numbers_of_larva = validated_data['numbers_of_larva']                
            )

            for data in pond_image.getlist('pond_images'): 
                name = data.name                      
                CyclePondImage.objects.create(images=cycle_instance, image_name=name, image=data)
                
            
            for data in seed_image.getlist('seed_images'): 
                name = data.name                      
                CycleSeedImage.objects.create(images=cycle_instance, image_name=name, image=data)    
                
            return cycle_instance
        
    def update(self, instance, validated_data):

        pond_image = self.context.get('view').request.FILES
        seed_image = self.context.get('view').request.FILES
        instance.Pond = validated_data.get('Pond',instance.Pond)
        instance.species = validated_data.get('species',instance.species)
        instance.speciesPlStage = validated_data.get('speciesPlStage',instance.speciesPlStage)       
        instance.seed_company = validated_data.get('seed_company',instance.seed_company)
        instance.invest_amount = validated_data.get('invest_amount',instance.invest_amount)
        instance.pondPrep_cost = validated_data.get('pondPrep_cost',instance.pondPrep_cost)
        instance.description = validated_data.get('description',instance.description)
        instance.numbers_of_larva = validated_data.get('numbers_of_larva',instance.numbers_of_larva)
        instance.save()

        #here also we have to reference models fields only like 'pond_type=instance.pk'
        pondimage_with_same_profile_instance = CyclePondImage.objects.filter(images=instance.pk).values_list('id', flat=True)
        seedimage_with_same_profile_instance = CycleSeedImage.objects.filter(images=instance.pk).values_list('id', flat=True)


        for pondimage_id in pondimage_with_same_profile_instance:
            CyclePondImage.objects.filter(pk = pondimage_id).delete()        

        for seedimage_id in seedimage_with_same_profile_instance:
            CycleSeedImage.objects.filter(pk = seedimage_id).delete()        

        for data in pond_image.getlist('pond_images'): 
            name = data.name                      
            CyclePondImage.objects.create(images=instance, image_name=name, image=data)         


        for data in seed_image.getlist('seed_images'): 
            name = data.name                      
            CycleSeedImage.objects.create(images=instance, image_name=name, image=data)         


        return instance   