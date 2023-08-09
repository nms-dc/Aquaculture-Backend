from django.urls import URLPattern, path, include
from cycle.api.views import CyleView,PondPreparationMasterView,PondPreparationView
from rest_framework.routers import DefaultRouter

app_name = "cycle"

router = DefaultRouter()
router.register('cycleregist', CyleView)
router.register('pondprepmaster', PondPreparationMasterView)
router.register('pond-preparation', PondPreparationView)

urlpatterns = [
     path('', include(router.urls)),
]
