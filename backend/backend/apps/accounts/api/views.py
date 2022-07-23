from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from accounts.api.serializers import UserRegistrationSerializer


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
        else:
            data = serialize.errors
        return Response(data)
