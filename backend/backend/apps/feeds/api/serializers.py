
from rest_framework import serializers
from feeds.single_backup import farmdata
from feeds.models import FeedLots, Feeds, FeedType


class Feedsserializers(serializers.ModelSerializer):
    farmdata()
    class Meta:
        model = Feeds
        fields = "__all__"


class FeedLotsserializers(serializers.ModelSerializer):
    
    class Meta:
        model = FeedLots
        fields = "__all__"


class FeedTypeserializers(serializers.ModelSerializer):
    
    class Meta:
        model = FeedType
        fields = "__all__"