from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from accounts.models import User, create_username


from farms.api.serializers import farmSerializer



#post method
@api_view(['post', ])
def farmview(request):

    if request.method == 'POST':
        serialize = farmSerializer(data=request.data)
        return Response(request.data)
        if serialize.is_valid():
             serialize.save()
             #return Response(request.data)
             return Response(serialize.data)