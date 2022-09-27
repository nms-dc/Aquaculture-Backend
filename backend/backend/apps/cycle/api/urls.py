from django.urls import URLPattern, path, include
from cycle.api.views import CyleView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('cycleregist', CyleView)

urlpatterns = [
     path('', include(router.urls)),
]
