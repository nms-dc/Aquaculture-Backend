from django.urls import URLPattern, path, include
from ponds.api.views import PondView, PondMasterView, PondTypeView
from rest_framework.routers import DefaultRouter

app_name = "ponds"

router = DefaultRouter()
router.register('pondregist', PondView)
router.register('get-pondconstructType', PondMasterView)
router.register('get-pondtype', PondTypeView)

urlpatterns = [
    path('', include(router.urls)),
]
