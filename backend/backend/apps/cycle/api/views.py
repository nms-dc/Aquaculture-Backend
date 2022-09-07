from urllib.request import FancyURLopener
from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from accounts.models import User, create_username
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny

from cycle.models import Cycle
from cycle.api.serializers import CycleSerializer


class CyleView(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']
