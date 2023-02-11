from itertools import cycle
from rest_framework import serializers
from farms.models import Farms, FarmCertification, FarmImage, FeedLots, FarmAnalytics, FeedLotImage
from ponds.models import Ponds
from ponds.api.serializers import PondSummarySerializer, PondsSerializer, PondSummaryOnlySerializer
from accounts.models import User
from cycle.models import Cycle
from cycle.api.serializers import CycleSerializer
from company.models import Company, CompanyFeedType
from company.api.serializers import CompanySerializers, CompanyFeedTypeSerializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmImage
        fields = '__all__'


class CertifySerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmCertification
        fields = '__all__'


class FarmSummarySerializer(serializers.ModelSerializer):
    farm_images = ImageSerializer(many=True)

    class Meta:
        model = Farms
        fields = ["id", "farm_name", "description", "farm_images"]


class FarmPondRelationSerializer(serializers.ModelSerializer):
    ponds = serializers.SerializerMethodField()

    def get_ponds(self, obj):
        try:
            if Ponds.objects.filter(farm=obj).exists():
                ponds = Ponds.objects.filter(farm=obj.id)
                serializer = PondSummaryOnlySerializer(ponds, many=True).data
                return serializer
            else:
                return None
        except Ponds.DoesNotExist:
            return None

    class Meta:
        model = Farms
        fields = ["id", "farm_name", "description", "farm_images", "ponds"]


class FarmCycleRelationSerializer(serializers.ModelSerializer):
    ponds = serializers.SerializerMethodField()

    def get_ponds(self, obj):
        pond = Ponds.objects.filter(farm=obj.id)
        serializer = PondSummarySerializer(pond, many=True).data
        return serializer

    class Meta:
        model = Farms
        fields = ["id", "farm_name", "description", "farm_images", "ponds"]


class FarmSerializer(serializers.ModelSerializer):
    certificate = CertifySerializer(many=True, read_only=True)
    farm_images = ImageSerializer(many=True, read_only=True)
    fcr = serializers.SerializerMethodField(read_only=True)
    feed_data = serializers.SerializerMethodField(read_only=True)
    completed_cycle_count = serializers.SerializerMethodField(read_only=True)
    total_harvested_amt = serializers.SerializerMethodField(read_only=True)

    def get_completed_cycle_count(self, obj):
        all_ponds = Ponds.objects.filter(farm=obj).values_list('id', flat=True)
        all_cycles = Cycle.objects.filter(Pond_id__in=list(all_ponds))
        all_ponds_active_cycle = Ponds.objects.filter(farm=obj, is_active_pond=True).values_list('active_cycle_id', flat=True)
        total_completed_cycle = all_cycles.exclude(id__in=list(all_ponds_active_cycle)).count()
        return total_completed_cycle

    def get_total_harvested_amt(self, obj):
        already_exists_farm = FarmAnalytics.objects.filter(farm=obj.id)
        if already_exists_farm.exists():
            farm_analytics_instance = already_exists_farm.first()
            return farm_analytics_instance.harvest_amount
        else:
            return 0.0

    def get_fcr(self, obj):
        already_exists_farm = FarmAnalytics.objects.filter(farm=obj.id)
        if already_exists_farm.exists():
            farm_analytics_instance = already_exists_farm.first()
            if farm_analytics_instance.total_feed > 0:
                return farm_analytics_instance.harvest_amount / farm_analytics_instance.total_feed
            else:
                return 0.0

        else:
            return 0.0

    def get_feed_data(self, obj):
        try:
            if FeedLots.objects.filter(farm_id=obj).exists():
                ponds = FeedLots.objects.filter(farm_id=obj.id)
                serializer = FeedLotsSerializer(ponds, many=True).data
                return serializer

            else:
                return None
        except FeedLots.DoesNotExist:
            return None
        return 'hello world'

    class Meta:
        model = Farms
        fields = ["id", "farm_name", "farm_area", "phone", "address_line_one", "address_line_two", "state",
                  "town_village", "location", "description", "farm_images", "certificate", 'user', 'zipcode', 'district', 'fcr','feed_data', 'completed_cycle_count', 'total_harvested_amt']

    def create(self, validated_data):
        image_datas = self.context.get('view').request.FILES
        token = self.context.get('request').META.get('HTTP_AQUA_AUTH_TOKEN')
        user = User.objects.get(email=token)
        print('farm create validated data',validated_data)
        print('image_data details',image_datas)
        Farm_instance = Farms.objects.create(
                farm_name=validated_data['farm_name'],
                farm_area=validated_data['farm_area'],
                address_line_one=validated_data['address_line_one'],
                address_line_two=validated_data['address_line_two'],
                state=validated_data['state'],
                town_village=validated_data['town_village'],
                description=validated_data['description'],
                zipcode=validated_data['zipcode'],
                district=validated_data['district'],
                user=user
            )

        for image_data in image_datas.getlist('farm_images'):
            name = image_data.name
            FarmImage.objects.create(images=Farm_instance, image_name=name, image=image_data)

        for certify_data in image_datas.getlist('certificate'):
            name = certify_data.name
            FarmCertification.objects.create(certificates=Farm_instance, certificate_name=name, image=certify_data)

        return Farm_instance

    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        '''filtering the required data from the user payload request
        #here the farm_image_id is not a field defined in models from the user payload added extra'''
        data = self.context['request'].data.get('farm_images_id', None)
        '''#filtering 'farm_image_id' and converting it into an integer list'''
        int_image_id = []
        print('farm_image_id',data)
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_image_id.append(int(id))
        '''#filtering 'certi_image_id' and converting it into an integer list'''
        data = self.context['request'].data.get('certi_images_id', None)
        int_certi_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_certi_id.append(int(id))
        
        print('farm update validated data',validated_data)
        print('image_data details',image_datas)
        print('farm_image_id',int_image_id,'certificate_image_id',int_certi_id)
        instance.farm_name = validated_data.get('farm_name', instance.farm_name)
        instance.farm_area = validated_data.get('farm_area', instance.farm_area)
        instance.address_line_one = validated_data.get('address_line_one', instance.address_line_one)
        instance.address_line_two = validated_data.get('address_line_two', instance.address_line_two)
        instance.state = validated_data.get('state', instance.state)
        instance.town_village = validated_data.get('town_village', instance.town_village)
        instance.description = validated_data.get('description', instance.description)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.district = validated_data.get('district', instance.district)
        instance.save()

        certify_with_same_profile_instance = FarmCertification.objects.filter(certificates=instance.pk).values_list('id', flat=True)
        image_with_same_profile_instance = FarmImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        if len(int_certi_id) != 0:
            for delete_id in certify_with_same_profile_instance:
                if delete_id in int_certi_id:
                    FarmCertification.objects.filter(pk=delete_id).delete()

        if len(image_datas.getlist('certificate')) != 0:
            for certify_data in image_datas.getlist('certificate'):
                name = certify_data.name
                FarmCertification.objects.create(certificates=instance, certificate_name=name, image=certify_data)
        if len(int_image_id) != 0:
            for delete_id in image_with_same_profile_instance:
                if delete_id in int_image_id:
                    FarmImage.objects.filter(pk=delete_id).delete()
 
        if len(image_datas.getlist('farm_images')) != 0:
            for image_data in image_datas.getlist('farm_images'):
                name = image_data.name
                FarmImage.objects.create(images=instance, image_name=name, image=image_data)
        return instance


class FeedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedLotImage
        fields = '__all__'


class FeedLotsSerializer(serializers.ModelSerializer):
    #this field should be the same name with the related name of the foreign key reference
    feed_images = FeedImageSerializer(many=True, read_only=True)

    class Meta:
        model = FeedLots
        fields = '__all__' #['id', 'farm_id', 'lot_number', 'company_purchased_from', 'weight_of_each_bag_at_purchase', 'date_purchased',
        #           'date_shipped', 'date_received', 'bag_is_used', 'feed_cost', 'currency', 'feed_lot_type', 'feed_images']
    
    
    def create(self, validated_data):
        image_datas  = self.context.get('view').request.FILES
        print('feed create validated data',validated_data)
        print('image_data details',image_datas)
        Feed_instance = FeedLots.objects.create(
                farm_id=validated_data['farm_id'],
                lot_number=validated_data['lot_number'],
                company_purchased_from=validated_data['company_purchased_from'],
                weight_of_each_bag_at_purchase=validated_data['weight_of_each_bag_at_purchase'],
                date_purchased=validated_data['date_purchased'],
                date_shipped=validated_data['date_shipped'],
                date_received=validated_data['date_received'],
                bag_is_used=validated_data['bag_is_used'],
                feed_cost=validated_data['feed_cost'],
                currency=validated_data['currency'],
                feed_lot_type=validated_data['feed_lot_type'],
                company_feed_type = validated_data['company_feed_type'],
            )

        for image_data in image_datas.getlist('feed_images'):
            name = image_data.name
            FeedLotImage.objects.create(images=Feed_instance, image_name=name, image=image_data)

        return Feed_instance
    
    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        '''filtering the required data from the user payload request
        #here the farm_image_id is not a field defined in models from the user payload added extra'''
        data = self.context['request'].data.get('feed_image_id', None)
        '''#filtering 'feed_image_id' and converting it into an integer list'''
        int_image_id = []
        print('feed_image_id',data)
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_image_id.append(int(id))
        
        print('feed update validated data',validated_data)
        print('image_data details',image_datas)
        print('farm_image_id',int_image_id)
        instance.farm_id = validated_data.get('farm_id', instance.farm_id)
        instance.lot_number = validated_data.get('lot_number', instance.lot_number)
        instance.company_purchased_from = validated_data.get('company_purchased_from', instance.company_purchased_from)
        instance.weight_of_each_bag_at_purchase = validated_data.get('weight_of_each_bag_at_purchase', instance.weight_of_each_bag_at_purchase)
        instance.date_purchased = validated_data.get('date_purchased', instance.date_purchased)
        instance.date_shipped = validated_data.get('date_shipped', instance.date_shipped)
        instance.date_received = validated_data.get('date_received', instance.date_received)
        instance.bag_is_used = validated_data.get('bag_is_used', instance.bag_is_used)
        instance.feed_cost = validated_data.get('feed_cost', instance.feed_cost)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.feed_lot_type = validated_data.get('feed_lot_type', instance.feed_lot_type)
        instance.company_feed_type = validated_data.get('company_feed_type', instance.company_feed_type)
        instance.save()

        image_with_same_profile_instance = FeedLotImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        if len(int_image_id) != 0:
            for delete_id in image_with_same_profile_instance:
                if delete_id in int_image_id:
                    FeedLotImage.objects.filter(pk=delete_id).delete()
 
        if len(image_datas.getlist('feed_images')) != 0:
            for image_data in image_datas.getlist('feed_images'):
                name = image_data.name
                FeedLotImage.objects.create(images=instance, image_name=name, image=image_data)
        return instance


class FeedlotFilterSerializer(serializers.ModelSerializer):

    feeds = serializers.SerializerMethodField()

    def get_feeds(self, obj):
        farm = Farms.objects.filter(id=obj.id)
        serializers = FarmSerializer(farm, many=True).data
        result = []

        for feed in serializers:
            dic = dict(feed)
            feed_data = dic['feed_data']
            if feed_data:
                for data in feed_data:
                    dic_data = dict(data)
                    c_name = None
                    if dic_data['feed_lot_type'] == 'F':
                        c = Company.objects.filter(id=dic_data['company_purchased_from']).first()
                        company_type = CompanyFeedType.objects.filter(id = dic_data['company_feed_type'])
                        serialize_type = CompanyFeedTypeSerializers(company_type, many=True).data
                        if c != 0:
                            c_name = c.company_name
                        re_data = {'id': dic_data['id'], 'lotnumber': dic_data['lot_number'],
                                   'company_id': dic_data['company_purchased_from'], 'company_purchased_from': c_name,
                                   'company_type':serialize_type}
                        result.append(re_data)

        return result

    class Meta:
        model = Farms
        fields = ["id", 'feeds']


class FeedProSerializer(serializers.ModelSerializer):

    feeds = serializers.SerializerMethodField()
    def get_feeds(self, obj):
        farm = Farms.objects.filter(id=obj.id)
        serializers = FarmSerializer(farm, many=True).data
        result = []

        for feed in serializers:
            dic = dict(feed)
            feed_data = dic['feed_data']
            for data in feed_data:
                dic_data = dict(data)
                c_name = None
                if dic_data['feed_lot_type'] == 'P':
                    c = Company.objects.filter(id=dic_data['company_purchased_from']).first()
                    company_type = CompanyFeedType.objects.filter(id = dic_data['company_feed_type'])
                    serialize_type = CompanyFeedTypeSerializers(company_type, many=True).data
                    if c != 0:
                        c_name = c.company_name
                    re_data = {'id': dic_data['id'], 'lotnumber': dic_data['lot_number'],
                                'company_id': dic_data['company_purchased_from'], 'company_purchased_from': c_name,
                                'company_type':serialize_type}
                    result.append(re_data)

        return result

    class Meta:
        model = FeedLots
        fields = ["id", 'feeds']


class FeedAllSerializer(serializers.ModelSerializer):

    feeds = serializers.SerializerMethodField()

    def get_feeds(self, obj):
        farm = Farms.objects.filter(id=obj.id)
        serializers = FarmSerializer(farm, many=True).data
        result = []
        for feed in serializers:
            dic = dict(feed)
            feed_data = dic['feed_data']
            if feed_data is not None:
                for data in feed_data:
                    dic_data = dict(data)
                    if dic_data:
                        c = Company.objects.filter(id=dic_data['company_purchased_from']).first()
                        c = c.company_name
                        dic_data['company_name'] = c
                        
                    result.append(dic_data)

        return result

    class Meta:
        model = FeedLots
        fields = ["id", 'feeds']