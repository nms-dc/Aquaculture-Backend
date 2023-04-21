from rest_framework import viewsets
from feeds.models import Feeds,FeedLots,FeedType
from feeds.api.serializers import FeedLotsserializers, Feedsserializers, FeedTypeserializers


class FeedView(viewsets.ModelViewSet):
    queryset = Feeds.objects.all()
    serializer_class = Feedsserializers


class FeedlotView(viewsets.ModelViewSet):
    queryset = FeedLots.objects.all()
    serializer_class = FeedLotsserializers


class FeedTypeView(viewsets.ModelViewSet):
    queryset = FeedType.objects.all()
    serializer_class = FeedTypeserializers
