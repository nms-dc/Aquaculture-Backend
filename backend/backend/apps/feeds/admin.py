from django.contrib import admin
from feeds.models  import FeedType, Feeds

# Register your models here.
admin.site.register(FeedType)
admin.site.register(Feeds)
