from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from ponds.api.serializers import PondSerializer

@api_view(['post', ])
def pondview(request):

    if request.method == 'POST':
        serialize = PondSerializer(data=request.data)
        return Response(request.data)
        if serialize.is_valid():
             pond = serialize.save()
             #return Response(request.data)
             return Response(pond.data)
        else:
            return Response(serialize.errors)