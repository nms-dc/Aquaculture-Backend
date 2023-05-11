from django.contrib import admin
from feeds.models  import FeedType, Feeds, FeedPics

# Register your models here.
admin.site.register(FeedType)
admin.site.register(Feeds)
admin.site.register(FeedPics)
