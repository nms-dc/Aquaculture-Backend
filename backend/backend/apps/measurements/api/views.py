from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from measurements.models import MeasurementMaster, Measurement
from measurements.api.serializers import MeasurementSerializer, MeasurementTypeSerializer, MasterSerializer
from django.http import JsonResponse,  HttpResponse
from datetime import datetime, timedelta


class MeasureView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    authentication_classes = []
    permission_classes = [AllowAny]


class MasterView(viewsets.ModelViewSet):
    queryset = MeasurementMaster.objects.all()
    serializer_class = MasterSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['get']
