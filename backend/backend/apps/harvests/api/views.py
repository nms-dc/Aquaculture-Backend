from urllib.request import FancyURLopener
from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from accounts.models import User, create_username
from rest_framework import viewsets
from rest_framework.decorators import action

from harvests.models import Harvests 
from harvests.api.serializers import HarvestSerializer


class HarvestView(viewsets.ModelViewSet):
    queryset = Harvests.objects.all()
    serializer_class = HarvestSerializer
    
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']
