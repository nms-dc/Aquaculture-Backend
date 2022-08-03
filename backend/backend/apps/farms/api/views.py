from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from accounts.models import User, create_username
from rest_framework import viewsets

from farms.models import Farms, FarmCertification,FarmImage
from farms.api.serializers import FarmSerializer

#trying to work with post method
class FarmView(viewsets.ModelViewSet):
    queryset = Farms.objects.all()
    serializer_class = FarmSerializer
    http_method_names = ['post']




'''#post method
@api_view(['post' ])
def FarmView(request):

    if request.method == 'POST':
        serialize = farmSerializer(data=request.data)
        return Response(request.data)
        if serialize.is_valid():
             farm = serialize.save()
             #return Response(request.data)
             return Response(farm.data)
        else:
            return Response(serialize.errors)   
'''
'''
        if request.method == 'GET':
                data = Farms.objects.all()
                serialize = farmSerializer(data)
                return Response(serialize.data)




#trying:
@api_view(['post', ])
def farmImageview(request):

    if request.method == 'POST':
        serialize = FarmImageSerializer(data=request.data)
        if serialize.is_valid():
             farm = serialize.save()
             #return Response(request.data)
             return Response(farm.data)
        else:
            return Response(serialize.errors) 

@api_view(['post', ])
def farmCertificationview(request):

    if request.method == 'POST':
        serialize = FarmCertificationSerializer(data=request.data)
        
        if serialize.is_valid():
             farm = serialize.save()
             #return Response(request.data)
             return Response(farm.data)
        else:
            return Response(serialize.errors)             '''