from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from measurements.models import MeasurementType, Measurement
from measurements.api.serializers import MeasurementSerializer, MeasurementTypeSerializer, MasterSerializer
from django.http import JsonResponse,  HttpResponse
from datetime import datetime, timedelta



class MeasureView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    authentication_classes = []
    permission_classes = [AllowAny]


class MasterView(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MasterSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = [ 'get']


def notifications(request, *args, **kwargs):
    
    '''
	For each date since measurement cycle has started
	     select *  where Measurement where measurement_type not in (select measurement-type from MeasurementType and time.date = date)
		 pass this object to measurement Serializer

	'''
	
    date = datetime.now()
    date_1 =  datetime.now() - timedelta(days=1)
    date_2 =  datetime.now() - timedelta(days=2)
    date_3 =  datetime.now() - timedelta(days=3)
    date_4 =  datetime.now() - timedelta(days=4)
    l = {
    'date':date,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
    l1 = {
    'date':date_1,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
    l2 = {
    'date':date_2,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
   
    l3 = {
    'date':date_3,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
    l4 = {
    'date':date_4,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
   
    return JsonResponse([l,l1,l2,l3,l4], safe=False)
    
def measurements(request, *args, **kwargs):
    '''
    
	For each date since measurement cycle has started
	     select *  where Measurement where measurement_type in (select measurement-type
      from MeasurementType and time.date = date)
		 pass this object to measurement Serializer
	
    '''
    date = datetime.now()
    date_1 =  datetime.now() - timedelta(days=1)
    date_2 =  datetime.now() - timedelta(days=2)
    date_3 =  datetime.now() - timedelta(days=3)
    date_4 =  datetime.now() - timedelta(days=4)
    l = {
    'date':date,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
    l1 = {
    'date':date_1,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
    l2 = {
    'date':date_2,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
   
    l3 = {
    'date':date_3,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
    l4 = {
    'date':date_4,
    'measurements':[
		{
		  "id": 1,
		  "cycle": 17,
		  "measurementType": 'Temperature',
		  "value": 24,
		  "time": '2022-11-18T12:53:41+05:30',
		  "company": 'null',
		  "price_per_kg": 'null',		 
		  "measure_images": [
				     {
				      "id": 1,
				      "image_name": 'shiva_3',
				      "image": 'http://103.127.146.20:4000/aqua/measure_images/shiva_3.jpeg',
				     }
				    ],
		},
	       ],
    }
   
    return JsonResponse([l,l1,l2,l3,l4], safe=False)



  
   