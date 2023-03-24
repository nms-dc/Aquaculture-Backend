from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from measurements.models import MeasurementMaster, Measurement
from measurements.api.serializers import MeasurementSerializer, MeasurementTypeSerializer, MasterSerializer
from django.http import JsonResponse,  HttpResponse
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated


class MeasureView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    #authentication_classes = []
    permission_classes = [IsAuthenticated]


class MasterView(viewsets.ModelViewSet):
    queryset = MeasurementMaster.objects.all()
    serializer_class = MasterSerializer
    #authentication_classes = []
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
