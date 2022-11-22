from django.urls import URLPattern, path, include
from species.api.views import SpeciesView,SpeciesCategoryView
from rest_framework.routers import DefaultRouter

app_name = "species"

router = DefaultRouter()
router.register('get-species-list', SpeciesView)
router.register('categoryregist', SpeciesCategoryView)


urlpatterns = [
    path('', include(router.urls)),
]
