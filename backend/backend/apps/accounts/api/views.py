from rest_framework import status
import copy
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from django.http import HttpResponse
from accounts.models import User, create_username
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from accounts.api.serializers import UserRegistrationSerializer, UserBasicInfoSerializer, UserProfileInfoSerializer

@method_decorator(csrf_exempt)
def logout_view(request):
    logout(request)
    return HttpResponse("logout successful")


@api_view(['post', ])
@method_decorator(csrf_exempt)
def user_login_view(request):

    if request.method == 'POST':
        data = request.data
        user = authenticate(request, email=data['email'], password=data['password'])
        user_data = {}
        if user is not None:
            login(request, user)
            user_data = UserBasicInfoSerializer(instance=user).data
            return Response(user_data)
        else:
            user_data['message'] = "login failed"
            return Response(user_data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['post', ])
@method_decorator(csrf_exempt)
def user_registration_view(request):

    if request.method == 'POST':
        serialize = UserRegistrationSerializer(data=request.data)
        data = {}
        if serialize.is_valid():
            user = serialize.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = user.email
            data['phone_no'] = user.phone_no
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['username'] = user.username
            data['is_verified'] = user.is_verified
        else:
            data = serialize.errors
        return Response(data)


@api_view(['post', 'get', ])
@method_decorator(csrf_exempt)
def user_profile_view(request):

    if request.method == 'GET':
        token = request.headers.get('Aqua-Auth-Token', None)
        if token:
            try:
                user = User.objects.get(email=token)
                user_info = UserProfileInfoSerializer(instance=user).data
                return Response(user_info)
            except User.DoesNotExist:
                error = {}
                error['message'] = 'User Does Not Exists'
                return Response(error, status=status.HTTP_404_NOT_FOUND)
        else:
            error = {}
            error['message'] = 'Authentication not provided'
            return Response(error, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'POST':
        token = request.headers.get('Aqua-Auth-Token', None)
        data = {}
        if token:
            try:
                user = User.objects.get(email=token)
                data = copy.deepcopy(request.data)
                print('data', data)
                data.pop("username")
                data['username'] = create_username(data['email'])
                user_info = UserProfileInfoSerializer(instance=user, data=data)
                if user_info.is_valid():
                    user_info.save()
                return Response(user_info.data)
            except User.DoesNotExist:
                data['message'] = 'User Does Not Exists'
                return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            data['message'] = 'Authentication not provided'
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
