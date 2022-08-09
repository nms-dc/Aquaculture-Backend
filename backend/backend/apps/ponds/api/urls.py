from django.urls import URLPattern, path,include
from ponds.api.views import PondView
from rest_framework.routers import DefaultRouter

app_name = "ponds"

router = DefaultRouter()
router.register('pondregist',PondView)
#router dont need any pk while calling it

urlpatterns = [
    path('', include(router.urls)),
]
