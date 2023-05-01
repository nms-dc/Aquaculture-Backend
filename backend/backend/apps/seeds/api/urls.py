from django.urls import URLPattern, path, include
from seeds.api.views import SeedView
from rest_framework.routers import DefaultRouter

app_name = "seeds"

router = DefaultRouter()
router.register('seedregist', SeedView)


urlpatterns = [
     path('', include(router.urls)),
]
