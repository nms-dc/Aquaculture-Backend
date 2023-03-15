from django.urls import URLPattern, path, include
from harvests.api.views import HarvestView, AnimalView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('harvestregist', HarvestView)
router.register('animalregist', AnimalView)

urlpatterns = [
     path('', include(router.urls)),
]
