from django.urls import URLPattern, path, include
from farms.api.views import FarmView, FeedLotsView, CertifyView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('farmregist', FarmView)
router.register('feedregist', FeedLotsView)
router.register('certifyregist', CertifyView)

urlpatterns = [
     path('', include(router.urls)),
]
