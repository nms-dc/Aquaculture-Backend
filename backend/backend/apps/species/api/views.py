from re import I
from species.api.serializers import SpeciesSerializer, SpeciesCategorySerializer
from species.models import Species, SpeciesCategory
from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


class SpeciesView(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    #authentication_classes = []
    #permission_classes = [IsAuthenticated]


class SpeciesCategoryView(viewsets.ModelViewSet):
    queryset = SpeciesCategory.objects.all()
    serializer_class = SpeciesCategorySerializer
    #authentication_classes = []
    #permission_classes = [IsAuthenticated]
