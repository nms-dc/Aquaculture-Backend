
import datetime
from itertools import cycle
from rest_framework import serializers
from cycle.models import Cycle, CyclePondImage, CycleSeedImage, CycleAnalytics
from accounts.models import User
from harvests.models import Harvests
from harvests.api.serializers import HarvestSummarySerializer
from ponds.models import Ponds
import ponds.api.serializers as P
import datetime
from dateutil import parser
from measurements.models import Measurement, MeasurementMaster
from measurements.api.serializers import MeasurementSerializer, MeasurementcycleSerializer, MasterSerializer
from feeds.models import Feeds, FeedType, FeedPics
from feeds.api.serializers import Feedsserializers
#from cycle.single_backup import farmdata

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
            if Harvests.objects.filter(cycle=obj.id).exists():
                harvests = Harvests.objects.filter(cycle=obj)
                serializer = HarvestSummarySerializer(harvests, many=True).data
                return serializer
            else:
                return None
        except Harvests.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ["id", "species", "description", "harvest"]


class CycleMeasureRelationSerializer(serializers.ModelSerializer):
    measure = serializers.SerializerMethodField()

    def get_measure(self, obj):
        try:

            if Measurement.objects.filter(cycle=obj.id).exists():
                measured = Measurement.objects.filter(cycle=obj)
                serializer = MeasurementcycleSerializer(measured, many=True).data
                return serializer
            else:
                return None
        except Measurement.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ["id", "description", "measure"]


class CycleFeedSerializer(serializers.ModelSerializer):
    feeds = serializers.SerializerMethodField()

    def get_feeds(self, obj):
        try:
            if Feeds.objects.filter(cycle=obj.id).exists():
                #while we using 'values()' it will fetch the first record datas
                feeds = Feeds.objects.filter(cycle=obj.id)
                serialize = Feedsserializers(feeds, many=True).data
                return serialize
            else:
                return None
        except Feeds.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ["id", "description", "feeds"]


class CycleMeasureRelationSerializer(serializers.ModelSerializer):
    measure = serializers.SerializerMethodField()

    def get_measure(self, obj):
        try:

            if Measurement.objects.filter(cycle=obj.id).exists():
                measured = Measurement.objects.filter(cycle=obj)
                serializer = MeasurementcycleSerializer(measured, many=True).data
                return serializer
            else:
                return None
        except Measurement.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ["id", "description", "measure"]


class CycleSerializer(serializers.ModelSerializer):
    #farmdata()
    cycle_pond_images = PrepPondImageSerializer(many=True, read_only=True)
    seed_images = SeedImageSerializer(many=True, read_only=True)
    cycle_harvests = serializers.SerializerMethodField(read_only=True)
    total_harvested_amt = serializers.SerializerMethodField(read_only=True)
    total_avg_fcr = serializers.SerializerMethodField(read_only=True)
    total_feed = serializers.SerializerMethodField(read_only=True)
    total_probiotics = serializers.SerializerMethodField(read_only=True)

    def get_cycle_harvests(self, obj):
        try:
            if Cycle.objects.filter(id=obj.id).exists():
                harvests = Harvests.objects.filter(cycle=obj)
                serializer = HarvestSummarySerializer(harvests, many=True).data
                return serializer
            else:
                return None
        except Cycle.DoesNotExist:
            return None

    def get_total_harvested_amt(self, obj):
        already_exists_cycle = CycleAnalytics.objects.filter(cycle=obj, pond=obj.Pond, farm=obj.Pond.farm)
        if already_exists_cycle.exists():
            cycle_analytics_instance = already_exists_cycle.first()
            return cycle_analytics_instance.harvest_amount
        else:
            return 0.0
        
    def get_total_feed(self, obj):
        already_exists_cycle = CycleAnalytics.objects.filter(cycle=obj, pond=obj.Pond, farm=obj.Pond.farm)
        if already_exists_cycle.exists():
            cycle_analytics_instance = already_exists_cycle.first()
            return cycle_analytics_instance.total_feed
        else:
            return 0.0
        
    def get_total_probiotics(self, obj):
        already_exists_cycle = CycleAnalytics.objects.filter(cycle=obj, pond=obj.Pond, farm=obj.Pond.farm)
        if already_exists_cycle.exists():
            cycle_analytics_instance = already_exists_cycle.first()
            return cycle_analytics_instance.total_probiotics
        else:
            return 0.0

    def get_total_avg_fcr(self, obj):
        already_exists_cycle = CycleAnalytics.objects.filter(cycle=obj, pond=obj.Pond, farm=obj.Pond.farm)
        if already_exists_cycle.exists():
            cycle_analytics_instance = already_exists_cycle.first()
            if cycle_analytics_instance.total_feed > 0:
                return cycle_analytics_instance.harvest_amount / cycle_analytics_instance.total_feed
            else:
                return 0.0
        else:
            return 0.0

    class Meta:
        model = Cycle
        fields = ['id', 'Pond',"seeds", 'pondPrep_cost', 'description', 'lastupdatedt', 'seeding_qty', 'seeding_date', 'cycle_pond_images', 'seed_images',
                  'numbers_of_larva', 'cycle_harvests','pond_transfered_from', 'total_harvested_amt', "seed_transfer_date",
                   'total_avg_fcr', 'total_feed', 'total_probiotics', 'is_active', "species_weight", "created_by"]

    def create(self, validated_data):
        image_data = self.context.get('view').request.FILES
        cycle = Cycle.objects.filter(Pond = validated_data['pond_transfered_from'], is_active = True)
        cycle_data = CycleSerializer(cycle, many=True).data
        if cycle_data:
            seeding_date = cycle_data[0]['seeding_date']
        else:
            seeding_date = validated_data['seeding_date']

        cycle_instance = Cycle.objects.create(
            pondPrep_cost=validated_data['pondPrep_cost'],
            description=validated_data['description'],
            Pond=validated_data['Pond'],
            numbers_of_larva=validated_data['numbers_of_larva'],
            seeding_qty=validated_data['seeding_qty'],
            seeding_date=seeding_date,
            pond_transfered_from=validated_data['pond_transfered_from'],
            created_by = validated_data['created_by'],
            is_active = True,
            species_weight = validated_data['species_weight'],
            seeds=validated_data['seeds'],
            seed_transfer_date = validated_data['seed_transfer_date']
            )
        obj = Ponds.objects.get(pk=validated_data['Pond'].id)
        obj.is_active_pond = True
        obj.active_cycle_date = cycle_instance.seeding_date
        obj.active_cycle_id = cycle_instance.id
        obj.save()  

        if cycle_data:
            larva_count = cycle_data[0]['numbers_of_larva'] - validated_data['numbers_of_larva']
            data = Ponds.objects.filter(id = validated_data['pond_transfered_from'].id)
            if larva_count <= 0:
                cycle.update(numbers_of_larva = 0)
                cycle.update(is_active = False)
                data.update(is_active_pond = False)
                data.update(active_cycle_date = None)
                data.update(active_cycle_id = None)
            else:
                cycle.update(numbers_of_larva = larva_count)
     
                      
        for data in image_data.getlist('cycle_pond_images'):
            name = data.name
            CyclePondImage.objects.create(images=cycle_instance, image_name=name, image=data, created_by = validated_data['created_by'])

        for data in image_data.getlist('seed_images'):
            name = data.name
            CycleSeedImage.objects.create(images=cycle_instance, image_name=name, image=data, created_by = validated_data['created_by'])

        return cycle_instance

    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        data = self.context['request'].data.get('pond_images_id', None)
        '''#filtering 'pond_image_id' and converting it into an integer list'''
        int_Pimage_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_Pimage_id.append(int(id))

        data = self.context['request'].data.get('seed_images_id', None)
        '''#filtering 'seed_images_id' and converting it into an integer list'''
        int_Simage_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_Simage_id.append(int(id))
        str_created_date = self.context['request'].data.get('seeding_date', None)
        created_date = parser.parse(str_created_date)
        current_date = datetime.datetime.now()

        def numOfDays(date1, date2):
            return (date2 - date1).days
        doc = numOfDays(created_date, current_date)
        instance.Pond = validated_data.get('Pond', instance.Pond)
        instance.pondPrep_cost = validated_data.get('pondPrep_cost', instance.pondPrep_cost)
        instance.description = validated_data.get('description', instance.description)
        instance.numbers_of_larva = validated_data.get('numbers_of_larva', instance.numbers_of_larva)
        instance.seeding_qty = validated_data.get('seeding_qty', instance.seeding_qty)
        instance.seeding_date = validated_data.get('seeding_date', instance.seeding_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.pond_transfered_from = validated_data.get('pond_transfered_from', instance.pond_transfered_from)
        instance.species_weight = validated_data.get('species_weight', instance.species_weight)
        instance.seeds = validated_data.get('seeds', instance.seeds)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.seed_transfer_date = validated_data.get('seed_transfer_date', instance.seed_transfer_date)
        instance.save()

        pondimage_with_same_profile_instance = CyclePondImage.objects.filter(images=instance.pk).values_list('id', flat=True)
        seedimage_with_same_profile_instance = CycleSeedImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        if len(int_Pimage_id) != 0:
            for delete_id in pondimage_with_same_profile_instance:
                if delete_id in int_Pimage_id:
                    CyclePondImage.objects.filter(pk=delete_id).delete()
        if len(image_datas.getlist('cycle_pond_images')) != 0:
            for image_data in image_datas.getlist('cycle_pond_images'):
                name = image_data.name
                CyclePondImage.objects.create(images=instance, image_name=name, image=image_data, updated_by = validated_data.get('updated_by', instance.updated_by))
        if len(int_Simage_id) != 0:
            for delete_id in seedimage_with_same_profile_instance:
                if delete_id in int_Simage_id:
                    CycleSeedImage.objects.filter(pk=delete_id).delete()
        if len(image_datas.getlist('seed_images')) != 0:
            for image_data in image_datas.getlist('seed_images'):
                name = image_data.name
                CycleSeedImage.objects.create(images=instance, image_name=name, image=image_data, updated_by = validated_data.get('updated_by', instance.updated_by))
        obj = Ponds.objects.get(pk=validated_data['Pond'].id)
        obj.active_cycle_date = validated_data.get('seeding_date')
        obj.save()  
        return instance


class CycleMeasureSerializers(serializers.ModelSerializer):
    measurements = serializers.SerializerMethodField()

    def get_measurements(self, obj):
        try:
            if Measurement.objects.filter(cycle=obj).exists():
                measurement = Measurement.objects.filter(cycle=obj.id)
                serializer = MeasurementcycleSerializer(measurement, many=True).data
                data = []
                # print(obj)
                # print(serializer)
                for i in serializer:
                    dic = dict(i)                    
                    master_id = (dic['measurement_type'])
                    measure_data = MeasurementMaster.objects.filter(id = master_id)
                    measure_serialize = MasterSerializer(measure_data, many=True).data
                    measurment_type=measure_serialize[0]['measurement_type']
                    dic['measurement_type'] = measurment_type
                    data.append(dic)            
                data = sorted(data, key=lambda d: d['time'])
                data.reverse()
                return data
            else:
                return None
        except Measurement.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ["id", 'measurements']


class CyclefeedhistorySerializers(serializers.ModelSerializer):
    feeds = serializers.SerializerMethodField()

    def get_feeds(self, obj):
        try:
            if Feeds.objects.filter(cycle=obj).exists():
                feeds = Feeds.objects.filter(cycle=obj.id).values()
                #serializer = MeasurementcycleSerializer(measurement, many=True).data
                print((feeds))
                for feed_data in feeds:
                    feed_type_id = feed_data['feed_type_id']
                    feed_type = FeedType.objects.filter(id= feed_type_id).values()
                    feed_type =feed_type[0]['type']
                    
                    feed_data['feed_type'] = feed_type
                    return feed_data
            
            else:
                return None
        except Measurement.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ["id", 'feeds']