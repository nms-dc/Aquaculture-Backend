from django.urls import URLPattern, path, include
from feeds.api.views import FeedlotView, FeedView, FeedTypeView
from rest_framework.routers import DefaultRouter

app_name = "feeds"

router = DefaultRouter()
router.register('feedregist', FeedView)
router.register('feedlotregist', FeedlotView)
router.register('feedtyperegist', FeedTypeView)

urlpatterns = [
     path('', include(router.urls)),
]
