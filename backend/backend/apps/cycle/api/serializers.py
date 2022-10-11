import datetime
from rest_framework import serializers
from cycle.models import Cycle, CyclePondImage, CycleSeedImage
from accounts.models import User
from harvests.models import Harvests
from harvests.api.serializers import HarvestSummarySerializer
from ponds.models import Ponds


class PrepPondImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CyclePondImage
        fields = '__all__'


class SeedImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CycleSeedImage
        fields = '__all__'


class CycleHarvestRelationSerializer(serializers.ModelSerializer):
    harvest = serializers.SerializerMethodField()

    def get_harvest(self, obj):
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
        fields = ["id", "species", "description", "species_pl_stage", "harvest"]


class CycleSerializer(serializers.ModelSerializer):

    pond_images = PrepPondImageSerializer(many=True, read_only=True)
    seed_images = SeedImageSerializer(many=True, read_only=True)
    cycle_harvests = serializers.SerializerMethodField(read_only=True)

    def get_cycle_harvests(self, obj):
        try:
            if Cycle.objects.filter(id=obj.id).exists():
                harvests = Harvests.objects.filter(cycle=obj)
                serializer = HarvestSummarySerializer(harvests, many=True).data
                return serializer
            else:
                return None
        except Ponds.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ['id', 'Pond', 'species', 'species_pl_stage', 'seed_company', 'invest_amount', 'pondPrep_cost',
                  'description', 'lastupdatedt', 'seeding_qty', 'seeding_date', 'pond_images', 'seed_images',
                  'numbers_of_larva', 'cycle_harvests']

    def create(self, validated_data):
        image_data = self.context.get('view').request.FILES
        cycle_instance = Cycle.objects.create(
            species=validated_data['species'],
            species_pl_stage=validated_data['species_pl_stage'],
            invest_amount=validated_data['invest_amount'],
            pondPrep_cost=validated_data['pondPrep_cost'],
            description=validated_data['description'],
            Pond=validated_data['Pond'],
            seed_company=validated_data['seed_company'],
            numbers_of_larva=validated_data['numbers_of_larva'],
            seeding_qty=validated_data['seeding_qty'],
            seeding_date=validated_data['seeding_date']
            )
        obj = Ponds.objects.get(pk=validated_data['Pond'].id)
        obj.is_active_pond = True
        obj.active_cycle_date = datetime.date.today()
        obj.active_cycle_id = cycle_instance.id
        obj.save()

        for data in image_data.getlist('pond_images'):
            name = data.name
            CyclePondImage.objects.create(images=cycle_instance, image_name=name, image=data)

        for data in image_data.getlist('seed_images'):
            name = data.name
            CycleSeedImage.objects.create(images=cycle_instance, image_name=name, image=data)

        return cycle_instance

    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        data = self.context['request'].data.get('pond_images_id', None)
        '''#filtering 'pond_image_id' and converting it into an integer list'''
        int_Pimage_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            print('type of data', type(trim_image_id))
            for id in trim_image_id:
                print('id', int(id))
                int_Pimage_id.append(int(id))
        print(int_Pimage_id)

        data = self.context['request'].data.get('seed_images_id', None)
        '''#filtering 'seed_images_id' and converting it into an integer list'''
        int_Simage_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            print('type of data', type(trim_image_id))
            for id in trim_image_id:
                print('id', int(id))
                int_Simage_id.append(int(id))
        print(int_Simage_id)
        instance.Pond = validated_data.get('Pond', instance.Pond)
        instance.species = validated_data.get('species', instance.species)
        instance.species_pl_stage = validated_data.get('species_pl_stage', instance.species_pl_stage)
        instance.seed_company = validated_data.get('seed_company', instance.seed_company)
        instance.invest_amount = validated_data.get('invest_amount', instance.invest_amount)
        instance.pondPrep_cost = validated_data.get('pondPrep_cost', instance.pondPrep_cost)
        instance.description = validated_data.get('description', instance.description)
        instance.numbers_of_larva = validated_data.get('numbers_of_larva', instance.numbers_of_larva)
        instance.seeding_qty = validated_data.get('seeding_qty', instance.seeding_qty)
        instance.seeding_date = validated_data.get('seeding_date', instance.seeding_date)
        instance.save()

        pondimage_with_same_profile_instance = CyclePondImage.objects.filter(images=instance.pk).values_list('id', flat=True)
        seedimage_with_same_profile_instance = CycleSeedImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        if len(int_Pimage_id) != 0:
            for delete_id in pondimage_with_same_profile_instance:
                if delete_id in int_Pimage_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    CyclePondImage.objects.filter(pk=delete_id).delete()
        if len(image_datas.getlist('pond_images')) != 0:
            for image_data in image_datas.getlist('pond_images'):
                name = image_data.name
                CyclePondImage.objects.create(images=instance, image_name=name, image=image_data)
        if len(int_Simage_id) != 0:
            for delete_id in seedimage_with_same_profile_instance:
                if delete_id in int_Simage_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    CycleSeedImage.objects.filter(pk=delete_id).delete()
        if len(image_datas.getlist('seed_images')) != 0:
            for image_data in image_datas.getlist('seed_images'):
                name = image_data.name
                CycleSeedImage.objects.create(images=instance, image_name=name, image=image_data)
        return instance
