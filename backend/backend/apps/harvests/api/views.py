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
from rest_framework.permissions import AllowAny
from harvests.models import Harvests, AddAnimal
from harvests.api.serializers import HarvestSerializer, AddAnimalSerializers
from rest_framework.permissions import IsAuthenticated


class HarvestView(viewsets.ModelViewSet):
    queryset = Harvests.objects.all()
    serializer_class = HarvestSerializer
    #authentication_classes = []
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']


class AnimalView(viewsets.ModelViewSet):
    queryset = AddAnimal.objects.all()
    serializer_class = AddAnimalSerializers
    #authentication_classes = []
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']
