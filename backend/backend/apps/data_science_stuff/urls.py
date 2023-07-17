from django.urls import URLPattern, path, include
from data_science_stuff.views import location_finder, moon_status

app_name = "data_science_stuff"

urlpatterns = [
     path('locater', location_finder),
     path('moonstatus',moon_status)
]
