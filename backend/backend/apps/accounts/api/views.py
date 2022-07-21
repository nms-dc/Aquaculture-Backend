from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView


from accounts.api.serializers import  UserSignupSerializer, UserSinginserializer
from accounts.models import User


@api_view(['post','get' ])
def user_registration_view(request):

    if request.method == 'POST':
        serialize = UserRegistrationSerializer(data=request.data)
        data = {}
        if serialize.is_valid():
            user = serialize.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = user.email
            data['date_of_birth'] = user.date_of_birth
        else:
            data = serialize.errors
        return Response(data)
    

#approach-1

class signInView(APIView):
    def get(self,request):
        signIn = User.objects.all()
        serializer = UserSinginserializer(signIn, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSinginserializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)        



class signUpView(APIView):
    def get(self,request):
        signIn = User.objects.all()
        serializer = UserSignupSerializer(signIn, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSignupSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)        

'''
#type error while creating the object
#approach -2

@api_view(['POST','GET'])
def signInView(request):
    if request.method ==  'POST':
        serializer = UserSinginserializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()


            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['POST','GET'])
def signUpView(request):
    if request.method ==  'POST':
        serializer = UserSignupSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

#no error but not returning any data
#approch -5
class signInView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSinginserializer

    def get(self):
        instance = self.get_object()
        return instance.active_profile


class signUpView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer



#approach-4
##type error while creating the object

@api_view(['post', ])
def signInView(request):

    if request.method == 'POST':
        serialize = UserSinginserializer(data = request.data)
        data = {}

        if serialize.is_valid():
            serialize.save()
            data['response'] = 'Success'
        else:
            data['response'] = 'Failure'
        return Response(data)

@api_view(['post', ])
def signUpView(request):

    if request.method == 'POST':
        serialize = UserSignupSerializer(data = request.data)
        data = {}

        if serialize.is_valid():
            serialize.save()
            data['response'] = 'Success'
        else:
            data['response'] = 'Failure'
        return Response('faile')



#approach-3    
#type error while creating the object
class signInView(APIView):

    def post(self, request, format=None):
        # snippet = self.get_object(pk)    
        serializer = UserSinginserializer(data=request.data)
              
        if serializer.is_valid():
            serializer.save()
            data = {'response': 'Success'} #new user
        else:
            data = {'response': 'Failure'}    

        return Response(data)



class signUpView(APIView):

    def post(self, request,pk, *args,**kwargs):
        snippet = self.kwargs.get(pk)    
        serializer = UserSignupSerializer(snippet,data = request.data, many=True)
        res = {}
        if serializer.is_valid():
            serializer.save()
            res = {'response': 'Success'}

        else:
            res = {'response': 'Failure'}
        return Response(res)        '''