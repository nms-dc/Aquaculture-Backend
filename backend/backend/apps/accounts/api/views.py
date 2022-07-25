from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view


from accounts.api.serializers import UserRegistrationSerializer, UserBasicInfoSerializer


@api_view(['post', ])
def user_login_view(request):

    if request.method == 'POST':
        data = request.data
        user = authenticate(email=data['email'], password=data['password'])
        user_data = {}
        if user is not None:
            user_data = UserBasicInfoSerializer(instance=user).data
            return Response(user_data)
        else:
            user_data['message'] = "login failed"
            return Response(user_data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['post', ])
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
        else:
            data = serialize.errors
        return Response(data)
