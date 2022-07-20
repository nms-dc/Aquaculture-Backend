from rest_framework import serializers

from accounts.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        
        model = User
        fields = ['email', 'date_of_birth', 'password', 'password2']
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



class UserSinginserializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['username', 'password']

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['first_name','last_name','email','password','number']

    
