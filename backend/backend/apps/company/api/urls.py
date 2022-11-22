from django.urls import URLPattern, path, include
from company.api.views import CompanyView
from rest_framework.routers import DefaultRouter

app_name = "company"

router = DefaultRouter()
router.register('get-company-list', CompanyView)

urlpatterns = [
     path('', include(router.urls)),
]