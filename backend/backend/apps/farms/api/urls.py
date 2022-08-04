from django.urls import URLPattern, path,include
from farms.api.views import FarmView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('farmregist',FarmView)


urlpatterns = [
    # path('farmregist', farmview, name="farm/register"),
    # path('farmImage', farmImageview, name="farm/image"),
    # path('farmcertify', farmCertificationview, name="farm/certify")
     path('', include(router.urls)),
]
