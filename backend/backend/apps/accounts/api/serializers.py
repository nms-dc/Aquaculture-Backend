from rest_framework import serializers
from accounts.models import User, create_username
from farms.models import Farms


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'phone_no', 'password', 'password2', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        username = create_username(self.validated_data['email'])
        user = User(
            email=self.validated_data['email'],
            username=username,
            phone_no=self.validated_data['phone_no'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class UserBasicInfoSerializer(serializers.ModelSerializer):
    farm_id = serializers.SerializerMethodField()

    def get_farm_id(self, obj):
        try:
            if Farms.objects.filter(user=obj).exists():
                farm = Farms.objects.filter(user=obj).first()
                return farm.id
            else:
                return None
        except Farms.DoesNotExist:
            return None

    class Meta:
        model = User
        fields = ['email', 'phone_no', 'first_name', 'last_name', 'username', 'is_verified', 'farm_id']


class UserProfileInfoSerializer(serializers.ModelSerializer):
    is_verified = serializers.BooleanField(read_only=True)
    farm_id = serializers.SerializerMethodField()

    def get_farm_id(self, obj):
        try:
            if Farms.objects.filter(user=obj).exists():
                farm = Farms.objects.filter(user=obj).first()
                return farm.id
            else:
                return None
        except Farms.DoesNotExist:
            return None

    class Meta:
        model = User
        fields = ['email', 'phone_no', 'first_name', 'last_name', 'username', 'company_name', 'image',
                  'sic_gst_code', 'pan_no', 'address_one', 'address_two', 'pincode', 'website', 'is_verified', 'farm_id']
