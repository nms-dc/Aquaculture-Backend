from django.urls import URLPattern, path
from accounts.api.views import user_registration_view,signInview,signUpview,profileView
from rest_framework import routers
from django.conf.urls import url, include



app_name = "account"

router = routers.DefaultRouter()
#router.register(r'singup', UserSignupViews, basename = 'signup')
#router.register(r'signIn', SingInView, basename = 'signin')

urlpatterns = [
    path('register', user_registration_view, name="register"),
    path('signin', signInview.as_view(), name='signin'),
    path('signup', signUpview.as_view(), name='signup'),
    path('Profile', profileView.as_view(), name='profile')
]
