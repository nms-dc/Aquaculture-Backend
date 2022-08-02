from django.urls import URLPattern, path
from ponds.api.views import pondview

app_name = "ponds"


urlpatterns = [
    path('pondregist', pondview, name="pond/register"),
]
