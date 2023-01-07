from django.urls import path

from notifications.api import views
app_name = "notifications"

urlpatterns = [
    path('', views.api_home)
]
