from rest_framework import serializers
from notifications.models import Notifications
from measurements.models import Measurement
from measurements.api.serializers import MeasurementSerializer


class NotificationsSerializer(serializers.ModelSerializer):
    measurements= serializers.SerializerMethodField(read_only=True)
    
    def get_measurements(self, obj):
        measurement_data = self.context['request'].data.get('measurments', None)
        print(measurement_data)
        if measurement_data:
            id = Measurement.objects.filter(id=int(measurement_data)).values_list('id',flat=True).first()
            cycle = Measurement.objects.filter(id=int(measurement_data)).values_list('cycle',flat=True).first()
            measurementType = Measurement.objects.filter(id=int(measurement_data)).values_list('measurement_type',flat=True).first()
            value = Measurement.objects.filter(id=int(measurement_data)).values_list('value',flat=True).first()
            time = Measurement.objects.filter(id=int(measurement_data)).values_list('time',flat=True).first()
            company = Measurement.objects.filter(id=int(measurement_data)).values_list('company',flat=True).first()
            price_per_kg = Measurement.objects.filter(id=int(measurement_data)).values_list('price_per_kg',flat=True).first()
            measure_images = Measurement.objects.filter(id=int(measurement_data)).values_list('measure_images',flat=True).first()
            data = {'id':id,'cycle':cycle,'measurementType':measurementType,'value':value,'time':time,'company':company,
                    'price_per_kg':price_per_kg,'measure_images':measure_images}
            return data
        else:
            return 'not matched'


    class Meta:
        model = Notifications
        fields = ['id','date','measurements']
