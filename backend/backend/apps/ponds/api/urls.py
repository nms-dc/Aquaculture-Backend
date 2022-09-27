from django.urls import URLPattern, path, include
from ponds.api.views import PondView
from rest_framework.routers import DefaultRouter

app_name = "ponds"

router = DefaultRouter()
router.register('pondregist', PondView)

urlpatterns = [
    path('', include(router.urls)),
]
