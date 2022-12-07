from django.urls import URLPattern, path, include
from ponds.api.views import PondView, PondMasterView, PondTypeView, PondgraphView
from rest_framework.routers import DefaultRouter

app_name = "ponds"

router = DefaultRouter()
router.register('pondregist', PondView)
router.register('get-pondconstructType', PondMasterView)
router.register('get-pondtype', PondTypeView)
router.register('pondgraph', PondgraphView)

urlpatterns = [
    path('', include(router.urls)),
]
