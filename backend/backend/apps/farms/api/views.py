from urllib.request import FancyURLopener
from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from accounts.models import User, create_username
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from farms.models import Farms, FarmCertification, FarmImage
from farms.api.serializers import FarmSerializer, FarmSummarySerializer, FarmPondRelationSerializer
from django.views.decorators.csrf import csrf_exempt


class FarmView(viewsets.ModelViewSet):
    queryset = Farms.objects.all()
    serializer_class = FarmSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']

    @action(detail=True, methods=['get'], url_path='get-farm-summary',)
    @csrf_exempt
    def get_farm_summary(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FarmSummarySerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='get-related-ponds',)
    @csrf_exempt
    def get_related_ponds(self, request, *args, **kwargs):
        farm = self.get_object()
        result = FarmPondRelationSerializer(instance=farm, context={'request': request}).data
        return Response({"result": result})
