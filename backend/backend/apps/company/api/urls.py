from django.urls import URLPattern, path, include
from company.api.views import CompanyView, CompanyFeedView
from rest_framework.routers import DefaultRouter

app_name = "company"

router = DefaultRouter()
router.register('get-company-list', CompanyView)
router.register('get-companyfeed-list', CompanyFeedView)


urlpatterns = [
     path('', include(router.urls)),
]
