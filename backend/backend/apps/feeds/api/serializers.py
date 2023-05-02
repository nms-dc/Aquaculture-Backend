
from rest_framework import serializers
#from feeds.single_backup import farmdata
from feeds.models import FeedLots, Feeds, FeedType, FeedPics


class FeedImagessserializers(serializers.ModelSerializer):
    
    class Meta:
        model = FeedPics
        fields = "__all__"


class Feedsserializers(serializers.ModelSerializer):
    #farmdata()
    feed_image = serializers.SerializerMethodField()
    def get_feed_image(self,obj):
        feed_image = FeedPics.objects.filter(images = obj.id)
        serialize = FeedImagessserializers(feed_image, many=True).data
        return serialize

    class Meta:
        model = Feeds
        fields = "__all__"

    def create(self, validated_data):
        image_datas = self.context.get('view').request.FILES
        print('measurement create validated data',validated_data)
        print('image_data details',image_datas)
        measurement_instance = Feeds.objects.create(
            cycle=validated_data['cycle'],
            feed_type=validated_data['feed_type'],
            value=validated_data['value'],
            time=validated_data['time'],
            lot=validated_data['lot'],
            price_per_kg=validated_data['price_per_kg'],
            is_probiotic_mixed=validated_data['is_probiotic_mixed'],
            created_by = validated_data['created_by']
            )

        for data in image_datas.getlist('feeds_images'):
            name = data.name
            FeedPics.objects.create(images=measurement_instance, image_name=name, image=data, created_by = validated_data['created_by'])

        return measurement_instance

    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        data = self.context['request'].data.get('measure_images_id', None)
        int_image_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_image_id.append(int(id))

        print('measurement update validated data',validated_data)
        print('image_data details',image_datas)
        print('feeds_image_id',int_image_id)
        instance.cycle = validated_data.get('cycle', instance.cycle)
        instance.feed_type = validated_data.get('feed_type', instance.feed_type)
        instance.value = validated_data.get('value', instance.value)
        instance.time = validated_data.get('time', instance.time)
        instance.lot = validated_data.get('lot', instance.lot)
        instance.price_per_kg = validated_data.get('price_per_kg', instance.price_per_kg)
        instance.is_probiotic_mixed = validated_data.get('is_probiotic_mixed', instance.is_probiotic_mixed)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.save()

        feedimage_with_same_profile_instance = FeedPics.objects.filter(images=instance.pk).values_list('id', flat=True)

        if len(int_image_id) != 0:
            for delete_id in feedimage_with_same_profile_instance:
                if delete_id in int_image_id:
                    FeedPics.objects.filter(pk=delete_id).delete()
        if len(image_datas.getlist('feeds_images')) != 0:
            for image_data in image_datas.getlist('feeds_images'):
                name = image_data.name
                FeedPics.objects.create(images=instance, image_name=name, image=image_data, updated_by = validated_data.get('updated_by', instance.updated_by))
        return instance

class FeedLotsserializers(serializers.ModelSerializer):
    
    class Meta:
        model = FeedLots
        fields = "__all__"


class FeedTypeserializers(serializers.ModelSerializer):
    
    class Meta:
        model = FeedType
        fields = "__all__"

