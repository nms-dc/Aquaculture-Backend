from django.urls import URLPattern, path, include
from farms.api.views import FarmView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('farmregist', FarmView)

urlpatterns = [
     path('', include(router.urls)),
]
