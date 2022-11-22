from django.urls import URLPattern, path, include
from graphs.api.views import Convertion_ratio,Cycle_Graphs,Harvest_Trend
from rest_framework.routers import DefaultRouter

app_name = "graphs"



urlpatterns = [
    path('convertionRatio', Convertion_ratio),
    path('cycleGraphs', Cycle_Graphs),
    path('harvestTrend', Harvest_Trend)
]