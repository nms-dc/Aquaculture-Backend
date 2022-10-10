from itertools import count
from rest_framework import serializers
from cycle.models import Cycle, CyclePondImage, CycleSeedImage
from ponds.models import Ponds
from accounts.models import User
from harvests.models import Harvests, AddAnimal, HarvestAnimalImages, HarvestLogisticImages, HarvestPondImages
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


class HarvestSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Harvests
        fields = ['id','harvest_type', 'harvest_date', 'harvest_notes']


class HarvestSerializer(serializers.ModelSerializer):
    ani_images = AnimalImageSerializer(many=True, read_only=True)
    pond_images = HarvestPondImageSerializer(many=True, read_only=True)
    log_images = LogImageSerializer(many=True, read_only=True)

    class Meta:
        model = Harvests
        fields = '__all__'

    def create(self, validated_data):
        image_data = self.context.get('view').request.FILES
        harvest_instance = Harvests.objects.create(
            harvest_type=validated_data['harvest_type'],
            total_kgs=validated_data['total_kgs'],
            temperature=validated_data['temperature'],
            sold_to=validated_data['sold_to'],
            harvest_notes=validated_data['harvest_notes'],
            harvest_cost=validated_data['harvest_cost'],
            cycle=validated_data['cycle'],
            animal_count_1=validated_data['animal_count_1'],
            total_kg_1=validated_data['total_kg_1'],
            price_kg_1=validated_data['price_kg_1'],
            is_chill_kill=validated_data['is_chill_kill']
        )

        if validated_data['harvest_type'] == 'F':
            obj_cycle = Cycle.objects.get(id=int(validated_data.get('cycle').id))
            obj_pond = Ponds.objects.get(id=obj_cycle.Pond.id)
            obj_pond.is_active_pond = False
            obj_pond.active_cycle_id = None
            obj_pond.save()

        if validated_data['harvest_type'] == 'P':
            obj_cycle = Cycle.objects.get(id=int(validated_data.get('cycle').id))
            obj_pond = Ponds.objects.get(id=obj_cycle.Pond.id)
            obj_cycle.harvest_id = harvest_instance.id
            obj_pond.no_of_harvests = obj_pond.no_of_harvests + 1
            obj_cycle.save()
            obj_pond.save()

        for data in image_data.getlist('ani_images'):
            name = data.name
            HarvestAnimalImages.objects.create(images=harvest_instance, image_name=name, image=data)
        for data in image_data.getlist('pond_images'):
            name = data.name
            HarvestPondImages.objects.create(images=harvest_instance, image_name=name, image=data)
        for data in image_data.getlist('log_images'):
            name = data.name
            HarvestLogisticImages.objects.create(images=harvest_instance, image_name=name, image=data)

        return harvest_instance

    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        
        
        data = self.context['request'].data.get('ani_images_id', None)
        int_animal_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_animal_id.append(int(id))
        
        data = self.context['request'].data.get('pond_images_id', None)
        int_pond_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_pond_id.append(int(id))
        
        data = self.context['request'].data.get('log_images_id', None)
        int_log_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_log_id.append(int(id))

        
        
        instance.harvest_type = validated_data.get('harvest_type', instance.harvest_type)
        instance.total_kgs = validated_data.get('total_kgs',  instance.total_kgs)
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.sold_to = validated_data.get('sold_to', instance.sold_to)
        instance.harvest_notes = validated_data.get('harvest_notes', instance.harvest_notes)
        instance.harvest_cost = validated_data.get('harvest_cost', instance.harvest_cost)
        instance.cycle = validated_data.get('cycle', instance.cycle)
        instance.animal_count_1 = validated_data.get('animal_count_1', instance.animal_count_1)
        instance.total_kg_1 = validated_data.get('total_kg_1', instance.total_kg_1)
        instance.price_kg_1 = validated_data.get('price_kg_1', instance.price_kg_1)
        instance.is_chill_kill = validated_data.get('is_chill_kill', instance.is_chill_kill)
        instance.save()

        if validated_data['harvest_type'] == 'F':
            obj_cycle = Cycle.objects.get(id=int(validated_data.get('cycle').id))
            obj_pond = Ponds.objects.get(id=obj_cycle.Pond.id)
            obj_pond.is_active_pond = False
            obj_pond.active_cycle_id = None
            obj_pond.save()

        if validated_data['harvest_type'] == 'P':
            obj_cycle = Cycle.objects.get(id=int(validated_data.get('cycle').id))
            obj_cycle.harvest_id = instance.id
            obj_pond.save()

        pondimage_with_same_profile_instance = HarvestPondImages.objects.filter(images=instance.pk).values_list('id', flat=True)
        ani_image_with_same_profile_instance = HarvestAnimalImages.objects.filter(images=instance.pk).values_list('id', flat=True)
        log_image_with_same_profile_instance = HarvestLogisticImages.objects.filter(images=instance.pk).values_list('id', flat=True)

        
        if len(int_animal_id) != 0:
            for delete_id in ani_image_with_same_profile_instance:
                if delete_id in int_animal_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    
                    HarvestAnimalImages.objects.filter(pk=delete_id).delete()
        
        '''this if block should come after the deletion block which is the abouve if block
            then only this data will get delete after insertion of data base if we put the below
            if block above into the deletion if which above if block this new image also will get deleted'''
        if len(image_datas.getlist('ani_images')) != 0:  
            
            for image_data in image_datas.getlist('ani_images'):
                name = image_data.name
                HarvestAnimalImages.objects.create(images=instance, image_name=name, image=image_data)
                
        if len(int_pond_id) != 0:
            for delete_id in pondimage_with_same_profile_instance:
                if delete_id in int_pond_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    
                    HarvestPondImages.objects.filter(pk=delete_id).delete()
        
        '''this if block should come after the deletion block which is the abouve if block
            then only this data will get delete after insertion of data base if we put the below
            if block above into the deletion if which above if block this new image also will get deleted'''
        if len(image_datas.getlist('pond_images')) != 0:  
            
            for image_data in image_datas.getlist('pond_images'):
                name = image_data.name
                HarvestPondImages.objects.create(images=instance, image_name=name, image=image_data)
                
        if len(int_log_id) != 0:
            for delete_id in log_image_with_same_profile_instance:
                if delete_id in int_log_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    
                    HarvestLogisticImages.objects.filter(pk=delete_id).delete()
        
        '''this if block should come after the deletion block which is the abouve if block
            then only this data will get delete after insertion of data base if we put the below
            if block above into the deletion if which above if block this new image also will get deleted'''
        if len(image_datas.getlist('log_images')) != 0:  
            
            for image_data in image_datas.getlist('log_images'):
                name = image_data.name
                HarvestLogisticImages.objects.create(images=instance, image_name=name, image=image_data)                   
               

        return instance
