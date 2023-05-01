from rest_framework import viewsets
from seeds.models import Seeds, SeedImage
from seeds.api.serializers import Seedserializers


class SeedView(viewsets.ModelViewSet):
    queryset = Seeds.objects.all()
    serializer_class = Seedserializers

