from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework import viewsets
from ponds.models import PondType, PondConstructType, Ponds
from ponds.api.serializers import PondsSerializer, PondSummarySerializer, PondCycleRelationSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from cycle.models import Cycle


class PondView(viewsets.ModelViewSet):
    queryset = Ponds.objects.all()
    serializer_class = PondsSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    @action(detail=True, methods=['get'], url_path='get-pond-summary',)
    @csrf_exempt
    def get_Pond_summary(self, request, *args, **kwargs):
        pond = self.get_object()
        result = PondSummarySerializer(instance=pond, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='get-cycle-history',)
    @csrf_exempt
    def get_cycle_history(self, request, *args, **kwargs):
        pond = self.get_object()
        result = PondCycleRelationSerializer(instance=pond, context={'request': request}).data
        return Response({"result": result})
