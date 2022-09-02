from rest_framework import status
import copy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework import viewsets
from ponds.models import PondType,PondConstructType,Ponds
from ponds.api.serializers import PondsSerializer, PondSummarySerializer
   

class PondView(viewsets.ModelViewSet):
    queryset = Ponds.objects.all()
    serializer_class = PondsSerializer
    http_method_names = ['post','get','patch']    


    @action(detail=True, methods=['get'], url_path='get-pond-summary',)
    def get_Pond_summary(self, request, *args, **kwargs):
        pond = self.get_object()
        result = PondSummarySerializer(instance=pond, context={'request': request}).data
        return Response({"result": result})
