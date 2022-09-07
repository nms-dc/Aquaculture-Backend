from django.urls import URLPattern, path,include
from harvests.api.views import HarvestView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('harvestregist',HarvestView)


urlpatterns = [
   
     path('', include(router.urls)),
]
