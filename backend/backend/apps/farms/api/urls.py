from django.urls import URLPattern, path,include
from farms.api.views import FarmView
from rest_framework.routers import DefaultRouter

app_name = "farms"

router = DefaultRouter()
router.register('farmregist',FarmView)
from django.conf.urls.static import static
from  django.conf import settings


urlpatterns = [
    # path('farmregist', farmview, name="farm/register"),
    # path('farmImage', farmImageview, name="farm/image"),
    # path('farmcertify', farmCertificationview, name="farm/certify")
     path('', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
