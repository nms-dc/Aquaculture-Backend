from django.urls import URLPattern, path, include
from measurements.api.views import MeasureView, MasterView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('measureregist', MeasureView)
router.register('get-master', MasterView)

urlpatterns = [
     path('', include(router.urls)),
     # path('pk/get-notifications', notifications),
     # path('pk/get-measurements', measurements),
]
