from django.urls import URLPattern, path
from accounts.api.views import user_registration_view, user_login_view


app_name = "account"


urlpatterns = [
    path('register', user_registration_view, name="register"),
    path('login', user_login_view, name="login"),
]
