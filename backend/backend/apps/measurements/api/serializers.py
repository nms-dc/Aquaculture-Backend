from attr import fields
from rest_framework import serializers
from measurements.models import Measurement, MeasurementMaster, MeasurementPics
from farms.models import FeedLots
import farms.api.serializers as se
from company.models import Company
from company.api.serializers import CompanySerializers
#from measurements.single_backup import farmdata


class MeasurementPicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasurementPics
        fields = '__all__'


class MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasurementMaster
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    #farmdata()
    measure_images = MeasurementPicsSerializer(many=True, read_only=True)
    measurement_description = serializers.SerializerMethodField(read_only=True)

    def get_measurement_description(self, obj):
        measurement_type_var = self.context['request'].data.get('measurement_type', None)
        if measurement_type_var:
            return MeasurementMaster.objects.filter(measurement_type=measurement_type_var).values_list('measurement_description',
                                                                                              flat=True).first()
        else:
            return None

    # def get_lot_number(self, obj):
    #     measurement_type_var = self.context['request'].data.get('measurement_type', None)
    #     # do a filter of measurement master on measurement_type_var
    #     # if measurement_type == feeds or measurement_type == probiotics 
    #     if measurement_type_var == '4' or measurement_type_var == '8':
    #         data = FeedLots.objects.filter(id=measurement_type_var).values_list('lot_number', flat=True).first()
    #         return data
    #     else:
    #         return None

    # def get_company_name(self, obj):
    #     measurement_type_var = self.context['request'].data.get('measurement_type', None)
    #     if measurement_type_var == '4' or measurement_type_var == '8':
    #         c = Company.objects.filter(id=measurement_type_var)
    #         com = CompanySerializers(c, many=True).data
    #         for i in com:
    #             c_dic = dict(i)
    #             c_name = c_dic['company_name']
    #             print(c_name)
    #         return c_name
    #     else:
    #         return None

    class Meta:
        model = Measurement
        fields = ['id', 'cycle', 'value', 'time', 'measurement_type', 'measurement_description',
                  'measure_images', 'notes', 'created_by']

    
    def create(self, validated_data):
        image_datas = self.context.get('view').request.FILES
        print('measurement create validated data',validated_data)
        print('image_data details',image_datas)
        measurement_instance = Measurement.objects.create(
            cycle=validated_data['cycle'],
            measurement_type=validated_data['measurement_type'],
            value=validated_data['value'],
            time=validated_data['time'],
            notes=validated_data['notes'],
            created_by=validated_data['created_by']
            )

        for data in image_datas.getlist('measure_images'):
            name = data.name
            MeasurementPics.objects.create(images=measurement_instance, image_name=name, image=data, created_by=validated_data['created_by'])

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
        print('measure_image_id',int_image_id)
        instance.cycle = validated_data.get('cycle', instance.cycle)
        instance.measurement_type = validated_data.get('measurement_type', instance.measurement_type)
        instance.value = validated_data.get('value', instance.value)
        instance.time = validated_data.get('time', instance.time)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.save()

        measureimage_with_same_profile_instance = MeasurementPics.objects.filter(images=instance.pk).values_list('id', flat=True)

        if len(int_image_id) != 0:
            for delete_id in measureimage_with_same_profile_instance:
                if delete_id in int_image_id:
                    MeasurementPics.objects.filter(pk=delete_id).delete()
        if len(image_datas.getlist('measure_images')) != 0:
            for image_data in image_datas.getlist('measure_images'):
                name = image_data.name
                MeasurementPics.objects.create(images=instance, image_name=name, image=image_data, updated_by = validated_data.get('updated_by', instance.updated_by))
        return instance


class MeasurementTypeSerializer(serializers.ModelSerializer):
    measurement_types = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = MeasurementMaster
        fields = ['id', 'measurement_type', 'measurement_description', 'measurement_types']


class MeasurementcycleSerializer(serializers.ModelSerializer):
    measure_images = serializers.SerializerMethodField()
    measurement_unit = serializers.SerializerMethodField()
    
    def get_measure_images(self, obj):
        data = MeasurementPics.objects.filter(images = obj.id)
        serialize = MeasurementPicsSerializer(data, many=True).data
        return serialize

    def get_measurement_unit(self, obj):
        data = MeasurementMaster.objects.filter(measurement_type = obj.measurement_type)
        serialize = MasterSerializer(data, many=True).data
        return serialize[0]['measurement_unit']
    
    class Meta:
        model = Measurement
        fields = ['id', 'cycle', 'value', 'time', 'lot', 'price_per_kg', 'measurement_type', 'is_probiotic_mixed', 'notes', 'measure_images', 'measurement_unit']

