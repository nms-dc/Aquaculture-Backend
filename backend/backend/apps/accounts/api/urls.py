from django.urls import URLPattern, path
from accounts.api.views import  signInView, signUpView
from rest_framework import routers
from django.conf.urls import url, include



app_name = "account"

router = routers.DefaultRouter()
#router.register(r'singup', UserSignupViews, basename = 'signup')
#router.register(r'signIn', SingInView, basename = 'signin')

urlpatterns = [
    #path('register', user_registration_view, name="register"),
    #url(r'^', include(router.get_urls())),
    #path('signin', signInView.as_view({'post': 'list','get':'list'}),name = 'signin'),
    #path('signup', signUpView.as_view({'post': 'list', 'get':'list'}), name = 'signup')
    #path('signin', signInView, name = 'signin'),
    #path('signup', signUpView, name = 'signup')
    path('signin', signInView.as_view(),name = 'signin'),
    path('signup', signUpView.as_view(), name = 'signup')


]
