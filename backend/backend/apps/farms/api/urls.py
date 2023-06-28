from django.urls import URLPattern, path, include
from farms.api.views import FarmView, FeedLotsView, CertifyView, LotTypeView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('farmregist', FarmView)
router.register('feedregist', FeedLotsView)
router.register('certifyregist', CertifyView)
router.register('lottyperegist', LotTypeView)

urlpatterns = [
     path('', include(router.urls)),
]
