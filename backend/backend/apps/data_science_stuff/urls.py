from django.urls import URLPattern, path, include
from data_science_stuff.views import location_finder

app_name = "data_science_stuff"

urlpatterns = [
     path('locater', location_finder),
]