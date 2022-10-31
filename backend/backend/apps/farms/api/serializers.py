from itertools import cycle
from rest_framework import serializers
from farms.models import Farms, FarmCertification, FarmImage
from ponds.models import Ponds
from ponds.api.serializers import PondSummarySerializer, PondsSerializer, PondSummaryOnlySerializer
from accounts.models import User
from cycle.models import Cycle
from cycle.api.serializers import CycleSerializer


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
                ponds = Ponds.objects.filter(farm=obj)
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
        pond = Ponds.objects.filter(farm=obj)
        serializer = PondSummarySerializer(pond, many=True).data
        return serializer

    class Meta:
        model = Farms
        fields = ["id", "farm_name", "description", "farm_images", "ponds"]


class FarmSerializer(serializers.ModelSerializer):
    certificate = CertifySerializer(many=True, read_only=True)
    farm_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Farms
        fields = ["id", "farm_name", "farm_area", "phone", "address_line_one", "address_line_two", "state",
                  "town_village", "description", "farm_images", "certificate", 'user', 'zipcode', 'district']

    def create(self, validated_data):
        image_datas = self.context.get('view').request.FILES
        token = self.context.get('request').META.get('HTTP_AQUA_AUTH_TOKEN')
        user = User.objects.get(email=token)

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
        instance.farm_name = validated_data.get('farm_name', instance.farm_name)
        instance.farm_area = validated_data.get('farm_area', instance.farm_area)
        instance.address_line_one = validated_data.get('address_line_one', instance.address_line_one)
        instance.address_line_two = validated_data.get('address_line_two', instance.address_line_two)
        instance.state = validated_data.get('state', instance.state)
        instance.town_village = validated_data.get('town_village', instance.town_village)
        instance.description = validated_data.get('description', instance.description)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.district = validated_data.get('district', instance.district)
        # instance.user = user
        instance.save()

        certify_with_same_profile_instance = FarmCertification.objects.filter(certificates=instance.pk).values_list('id', flat=True)
        image_with_same_profile_instance = FarmImage.objects.filter(images=instance.pk).values_list('id', flat=True)

        '''old code
        if len(image_datas.getlist('certificate')) == 0:
            pass
        else:
            for certify_id in certify_with_same_profile_instance:
                FarmCertification.objects.filter(pk=certify_id).delete()

            for certify_data in image_datas.getlist('certificate'):
                name = certify_data.name
                FarmCertification.objects.create(certificates=instance, certificate_name=name, image=certify_data)'''

        if len(int_certi_id) != 0:
            for delete_id in certify_with_same_profile_instance:
                if delete_id in int_certi_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    FarmCertification.objects.filter(pk=delete_id).delete()

        '''this if block should come after the deletion block which is the abouve if block
            then only this data will get delete after insertion of data base if we put the below
            if block above into the deletion if which above if block this new image also will get deleted'''
        if len(image_datas.getlist('certificate')) != 0:
            for certify_data in image_datas.getlist('certificate'):
                name = certify_data.name
                FarmCertification.objects.create(certificates=instance, certificate_name=name, image=certify_data)
        if len(int_image_id) != 0:
            for delete_id in image_with_same_profile_instance:
                if delete_id in int_image_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    FarmImage.objects.filter(pk=delete_id).delete()

        '''this if block should come after the deletion block which is the abouve if block
            then only this data will get delete after insertion of data base if we put the below
            if block above into the deletion if which above if block this new image also will get deleted'''
        if len(image_datas.getlist('farm_images')) != 0:
            for image_data in image_datas.getlist('farm_images'):
                name = image_data.name
                FarmImage.objects.create(images=instance, image_name=name, image=image_data)
        return instance
