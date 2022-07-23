from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView  
from rest_framework import status
from rest_framework import generics


from accounts.api.serializers import UserRegistrationSerializer, UserSignupSerializer,\
                    UserSignInSerializers,profileSerializers
from accounts.models import User


@api_view(['post', ])
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


class signInview(APIView):


    #code that gets all the user data executes

    '''
    this docstring you can see on the response web page
    we have to insert the data then it will take  username as email then it will compare it to all
    the existing records email id then if some thing matches it will return true or else
    not authorised email message it will return'''
    '''
    def get(self, request):
        user = User.objects.all()
        serialize = profileInSerializers(user, many = True)
        return Response(serialize.data[0]['email'])'''#accessing a particular fields from serialized data

#this one for data normal response executes
    def post(self,request):
        serialize = UserSignInSerializers(data = request.data)
        
        if serialize.is_valid():
            pk = serialize.data['username']
            if User.objects.filter(email = pk).exists():
                data = User.objects.get(email = pk)
                res = profileSerializers(data)
                return Response(res.data)
            else:
                return Response('this %s mail is not authorised'%(pk))


class signUpview(APIView):  
    def post(self,request):
        serialize = UserSignupSerializer(data = request.data)
        
        #if serialize.is_valid():
            #serialize.save()
   
        return Response(serialize.data)

class profileView(APIView):
    
    """this docstring you can see on the response web page
    we have to insert the data then it will take  username as email then it will compare it to all
    the existing records email id then if some thing matches it will return true or else
    not authorised email message it will return"""

    
    #code that gets all the user data executes verify already data is ther or not
    
    ''' def get(self, request):
        user = User.objects.all()
        serialize = profileSerializers(user, many = True)
        return Response(serialize.data)'''

    def post(self,request):
        serialize = profileSerializers(data = request.data)
        
        if serialize.is_valid():
            pk = serialize.data['email']
            if User.objects.filter(email = pk).exists():
                data = User.objects.get(email = pk)
                res = profileSerializers(data)
                return Response(res.data)
            else:
                return Response('this %s mail is not authorised'%(pk))
        
#this one for normal response executes
'''
    def post(self,request):
        serialize = profileInSerializers(data = request.data)
        data = User.objects.all()
        if serialize.is_valid():
            return Response(serialize.data)          

'''





    
'''


class signInview(generics.ListAPIView):
    serializer_class = UserSignInSerializers

    def get_queryset(self):

        name = self.request.username 
        return User.objects.filter(email = name)   


@api_view(['post', ])
def signInview(request):

        email = request.POST['username']

        if User.objects.filter(email = email).exists():
            return True
        
        serialize = UserSignInSerializers(data=request.data)
        data = {}
        if serialize.is_valid():
            user = serialize.save()
            
            data['email'] = user.username
            
        else:
            data = serialize.errors
        return Response(data)  


class signUpview(APIView):
    
     def post(self,request):
        serializer = UserSignupSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) '''
