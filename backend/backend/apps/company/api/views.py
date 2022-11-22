from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from company.api.serializers import CompanySerializers
from company.models import Company


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['get']