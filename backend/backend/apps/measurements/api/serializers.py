from attr import fields
from rest_framework import serializers
from measurements.models import Measurement, MeasurementMaster, MeasurementPics, Nutrition


class NutritionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutrition
        fields = '__all__'


class MeasurementPicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasurementPics
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    nutrition_data = NutritionSerializer(many=True, read_only=True)
    measure_images = MeasurementPicsSerializer(many=True, read_only=True)
    measurement_description = serializers.SerializerMethodField()
    
    def get_measurement_description(sself, obj):
         return  "pH value"
    
    

    class Meta:
        model = Measurement
        fields = ['id', 'cycle', 'measurement_type', 'value', 'time',
                  'company', 'price_per_kg', 'nutrition_data', 'measure_images','measurement_description']

    def create(self, validated_data):
        image_datas = self.context.get('view').request.FILES
        measurement_instance = Measurement.objects.create(
            cycle=validated_data['cycle'],
            measurement_type=validated_data['measurement_type'],
            value=validated_data['value'],
            time=validated_data['time'],
            company=validated_data['company'],
            price_per_kg=validated_data['price_per_kg'],
            )

        for data in image_datas.getlist('measure_images'):
            name = data.name
            MeasurementPics.objects.create(images=measurement_instance, image_name=name, image=data)

        for data in image_datas.getlist('nutrition_data'):
            nutritions = self.context['request'].data.get('nutrition_data', None)
            nutrition_types = self.context['request'].data.get('nutrition_types', None)
            nutrition_descriptions = self.context['request'].data.get('nutrition_description', None)
            Nutrition.objects.create(feed_data=measurement_instance, nutrition=nutritions,
                                     nutrition_type=nutrition_types,
                                     nutrition_description=nutrition_descriptions)

        return measurement_instance

    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        data = self.context['request'].data.get('measure_images_id', None)
        '''filtering 'farm_image_id' and converting it into an integer list'''
        int_image_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_image_id.append(int(id))

        instance.cycle = validated_data.get('cycle', instance.cycle)
        instance.measurement_type = validated_data.get('measurement_type', instance.measurement_type)
        instance.value = validated_data.get('value', instance.value)
        instance.time = validated_data.get('time', instance.time)
        instance.company = validated_data.get('company', instance.company)
        instance.price_per_kg = validated_data.get('price_per_kg', instance.price_per_kg)
        instance.save()

        measureimage_with_same_profile_instance = MeasurementPics.objects.filter(images=instance.pk).values_list('id', flat=True)

        if len(int_image_id) != 0:
            for delete_id in measureimage_with_same_profile_instance:
                if delete_id in int_image_id:
                    '''if the id is there in database we should not delete'''
                    pass
                else:
                    MeasurementPics.objects.filter(pk=delete_id).delete()
        if len(image_datas.getlist('measure_images')) != 0:
            for image_data in image_datas.getlist('measure_images'):
                name = image_data.name
                MeasurementPics.objects.create(images=instance, image_name=name, image=image_data)
        for data in image_datas.getlist('nutrition_data'):
            Nutrition.objects.create(feed_data=instance)

        return instance


class MasterSerializer(serializers.ModelSerializer):
   # measurement_data = MeasurementSerializer(many=True, read_only=True)
    class Meta:
        model = MeasurementMaster
        fields = ['id', 'measurement_type', 'measurement_description' ]
