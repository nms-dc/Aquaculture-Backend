# from backend.backend.apps.cycle.models import Cycle
from rest_framework import serializers
from ponds.models import Ponds, PondImage, PondConstructType, PondType,PondGraphs
from harvests.models import Harvests
from accounts.models import User
from cycle.models import Cycle
from cycle.api.serializers import CycleSerializer



class PondImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PondImage
        fields = '__all__'


class PondSummarySerializer(serializers.ModelSerializer):
    pond_images = PondImageSerializer(many=True)
    cycle_harvests_count = serializers.SerializerMethodField(read_only=True)
    cycle_data = serializers.SerializerMethodField(read_only=True)

    def get_cycle_data(self, obj):
        cycle = Cycle.objects.filter(Pond=obj)
        serializer = CycleSerializer(cycle, many=True).data
        return serializer

    def get_cycle_harvests_count(self, obj):
        try:
            if Cycle.objects.filter(id=obj.active_cycle_id).exists():
                active_cycle = Cycle.objects.filter(id=obj.active_cycle_id).first()
                if Harvests.objects.filter(cycle=active_cycle, harvest_type='P').exists():
                    return Harvests.objects.filter(cycle=active_cycle, harvest_type='P').count()
                else:
                    return 0
            else:
                return 0
        except Ponds.DoesNotExist:
            return None

    class Meta:
        model = Ponds
        fields = ["id", "pond_name", "description", "pond_images", "pond_type", "is_active_pond", "doc", "cycle_harvests_count",
                  "cycle_data"]


class PondSummaryOnlySerializer(serializers.ModelSerializer):
    pond_images = PondImageSerializer(many=True)
    cycle_harvests_count = serializers.SerializerMethodField(read_only=True)

    def get_cycle_harvests_count(self, obj):
        try:
            if Cycle.objects.filter(id=obj.active_cycle_id).exists():
                active_cycle = Cycle.objects.filter(id=obj.active_cycle_id).first()
                if Harvests.objects.filter(cycle=active_cycle, harvest_type='P').exists():
                    return Harvests.objects.filter(cycle=active_cycle, harvest_type='P').count()
                else:
                    return 0
            else:
                return 0
        except Ponds.DoesNotExist:
            return None

    class Meta:
        model = Ponds
        fields = ["id", "pond_name", "description", "pond_images", "pond_type", "is_active_pond", "doc", "cycle_harvests_count"]


class PondCycleRelationSerializer(serializers.ModelSerializer):
    cycle = serializers.SerializerMethodField()

    def get_cycle(self, obj):
        try:
            if Cycle.objects.filter(Pond=obj).exists():
                cycle = Cycle.objects.filter(Pond=obj)
                serializer = CycleSerializer(cycle, many=True).data
                return serializer
            else:
                return None
        except Ponds.DoesNotExist:
            return None

    class Meta:
        model = Ponds
        fields = ["id", "pond_name", "description", "cycle"]


class PondsSerializer(serializers.ModelSerializer):

    pond_images = PondImageSerializer(many=True, read_only=True)

    class Meta:
        model = Ponds
        fields = ['id', 'pond_images', 'pond_name', 'pond_length', 'pond_breadth', 'pond_depth', 'pond_area',
                  'pond_capacity', 'description', 'pond_type', 'pond_construct_type', 'is_active_pond',
                  'active_cycle_id', 'farm', 'doc']

    def create(self, validated_data):
        pond_image = self.context.get('view').request.FILES
        pond_instance = Ponds.objects.create(
            pond_name=validated_data['pond_name'],
            pond_type=validated_data['pond_type'],
            pond_construct_type=validated_data['pond_construct_type'],
            pond_length=validated_data['pond_length'],
            pond_breadth=validated_data['pond_breadth'],
            pond_depth=validated_data['pond_depth'],
            pond_area=validated_data['pond_area'],
            pond_capacity=validated_data['pond_capacity'],
            description=validated_data['description'],
            farm=validated_data['farm']
            )

        for data in pond_image.getlist('pond_images'):
            name = data.name
            PondImage.objects.create(images=pond_instance, image_name=name, image=data)

        return pond_instance

    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        data = self.context['request'].data.get('pond_images_id', None)
        '''filtering 'farm_image_id' and converting it into an integer list'''
        int_image_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_image_id.append(int(id))

        instance.pond_name = validated_data.get('pond_name', instance.pond_name)
        instance.pond_type = validated_data.get('pond_type', instance.pond_type)
        instance.pond_construct_type = validated_data.get('pond_construct_type', instance.pond_construct_type)
        instance.pond_length = validated_data.get('pond_length', instance.pond_length)
        instance.pond_breadth = validated_data.get('pond_breadth', instance.pond_breadth)
        instance.pond_depth = validated_data.get('pond_depth', instance.pond_depth)
        instance.pond_area = validated_data.get('pond_area', instance.pond_area)
        instance.pond_capacity = validated_data.get('pond_capacity', instance.pond_capacity)
        instance.description = validated_data.get('description', instance.description)
        instance.farm = validated_data.get('farm', instance.farm)
        instance.save()

        pondimage_with_same_profile_instance = PondImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        if len(int_image_id) != 0:
            for delete_id in pondimage_with_same_profile_instance:
                if delete_id in int_image_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    PondImage.objects.filter(pk=delete_id).delete()

        if len(image_datas.getlist('pond_images')) != 0:
            for image_data in image_datas.getlist('pond_images'):
                name = image_data.name
                PondImage.objects.create(images=instance, image_name=name, image=image_data)

        return instance

class PondTypeSerializer(serializers.ModelSerializer):
    #pond_types = PondsSerializer(many=True, read_only = True)
    class Meta:
        model = PondType
        fields = ['id','name','desc']#, 'pond_types']

class PondConstructTypeSerializer(serializers.ModelSerializer):
    #Pond_construct = PondTypeSerializer(many=True,read_only = True)
    class Meta:
        model = PondConstructType
        fields = ['id','construct_type']#,'Pond_construct']
        
class PondGraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondGraphs
        fields = ['id','farm','abw','pond','total_feed','time']        
        

class PondGraphRelationSerializer(serializers.ModelSerializer):
    abw_data = serializers.SerializerMethodField()

    def get_abw_data(self, obj):
        try:
            if PondGraphs.objects.filter(pond=obj).exists():
                ponds = PondGraphs.objects.filter(pond=obj)
                serializer = PondGraphSerializer(ponds, many=True).data
                data = []
                for i in serializer:
                    #converting an ordereddict to normal dictionary
                    dic = dict(i)
                    data.append({'date':dic['time'],'abw_data':dic['abw']})
                    print(data)
                data = sorted(data, key = lambda d: d['date'])
                return data
            
            else:
                return None
        except Ponds.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ["id", 'abw_data']        
        
        
class PondGraphFCRSerializer(serializers.ModelSerializer):
    fcr_data = serializers.SerializerMethodField()

    def get_fcr_data(self, obj):
        try:
            if PondGraphs.objects.filter(pond=obj).exists():
                ponds = PondGraphs.objects.filter(pond=obj)
                serializer = PondGraphSerializer(ponds, many=True).data
                data = []
                for i in serializer:
                    #converting an ordereddict to normal dictionary
                    dic = dict(i)
                    abw = dic['abw']
                    total_feed = dic['total_feed']
                    fcr = abw/total_feed
                    data.append({'date':dic['time'],'fcr_data':fcr})
                    print(data)
                data = sorted(data, key = lambda d: d['date'])
                return data
            
            else:
                return None
        except Ponds.DoesNotExist:
            return None

    class Meta:
        model = Cycle
        fields = ["id", 'fcr_data']