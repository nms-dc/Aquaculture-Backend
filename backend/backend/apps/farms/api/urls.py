from django.urls import URLPattern, path
from farms.api.views import farmview

app_name = "farms"


urlpatterns = [
    path('farmregist', farmview, name="farm/register"),
    
]
