from urllib.request import FancyURLopener
from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from accounts.models import User, create_username
from rest_framework import viewsets
from rest_framework.decorators import action

from cycle.models import Cycle
from cycle.api.serializers import CycleSerializer


class CyleView(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
    
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']
