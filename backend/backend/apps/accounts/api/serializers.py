from rest_framework import serializers

from accounts.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        
        model = User
        fields = ['email', 'date_of_birth', 'password', 'password2','first_name','last_name','number']
        extra_kwargs = {
             'password': {'write_only': True}
        }

    def save(self):
        
        #if you want to save both fields use this method
        user = User(
            email=self.validated_data['email'],
            date_of_birth=self.validated_data['date_of_birth'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user



class UserSignInSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    '''def save(self):
        user = User(
                username=self.validated_data['username'],
                password=self.validated_data['password']
                

            )    
        user.save()
        return user'''


class UserSignupSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','number']
            
    '''def save(self):
        user = User(
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                email=self.validated_data['email'],
                password=self.validated_data['password'],
                number=self.validated_data['number']


            )    
        user.save()
        return user'''

class profileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','full_name','company_name','gst_number','pan_number','address_line_1',
        'address_line_2','pincode','website']        