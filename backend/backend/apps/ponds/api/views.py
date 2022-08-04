from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from rest_framework import viewsets
from ponds.models import Ponds
from ponds.api.serializers import PondSerializer

class PondView(viewsets.ModelViewSet):
    queryset = Ponds.objects.all()
    serializer_class = PondSerializer
    http_method_names = ['post']
