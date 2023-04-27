from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from company.api.serializers import CompanySerializers, CompanyFeedTypeSerializers, getFeedTypeSerializers \
    , CompanyFeedSerializers, CompanyProbioticsSerializers, CompanySeedsSerializers, CompanyFeedProSerializers
    
from company.models import Company, CompanyFeedType
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    authentication_classes = []
    #permission_classes = [IsAuthenticated]
    http_method_names = ['get','post']
    @action(detail=True, methods=['get'], url_path='types',)
    @csrf_exempt
    def get_types(self, request, *args, **kwargs):
        farm = self.get_object()
        result = getFeedTypeSerializers(instance=farm, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='F',)
    @csrf_exempt
    def get_F(self, request, *args, **kwargs):
        farm = self.get_object()
        result = CompanyFeedSerializers(instance=farm, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='P',)
    @csrf_exempt
    def get_P(self, request, *args, **kwargs):
        farm = self.get_object()
        result = CompanyProbioticsSerializers(instance=farm, context={'request': request}).data
        return Response({"result": result})
    
    @action(detail=True, methods=['get'], url_path='S',)
    @csrf_exempt
    def get_S(self, request, *args, **kwargs):
        farm = self.get_object()
        result = CompanySeedsSerializers(instance=farm, context={'request': request}).data
        return Response({"result": result})
    
    @action(detail=True, methods=['get'], url_path='F-P',)
    @csrf_exempt
    def get_F_P(self, request, *args, **kwargs):
        farm = self.get_object()
        result = CompanyFeedProSerializers(instance=farm, context={'request': request}).data
        return Response({"result": result})


class CompanyFeedView(viewsets.ModelViewSet):
    queryset = CompanyFeedType.objects.all()
    serializer_class = CompanyFeedTypeSerializers
    authentication_classes = []
    #permission_classes = [IsAuthenticated]
    http_method_names = ['get','post', 'patch', 'delete']

