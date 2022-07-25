from django.urls import URLPattern, path
from accounts.api.views import user_registration_view, user_login_view, user_profile_view, logout_view


app_name = "account"


urlpatterns = [
    path('register', user_registration_view, name="register"),
    path('login', user_login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('profile', user_profile_view, name="profile"),
]
