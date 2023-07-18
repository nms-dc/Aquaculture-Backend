from rest_framework import serializers
from accounts.models import User, create_username, Roles
from farms.models import Farms
#from accounts.api.single_backup import userdata


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone_no', 'password', 'password2', 'first_name', 'last_name']
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
            if Farms.objects.filter(created_by=obj).exists():
                farm = Farms.objects.filter(created_by=obj).first()
                return farm.id
            else:
                return None
        except Farms.DoesNotExist:
            return None

    class Meta:
        model = User
        fields = ['id', 'email', 'phone_no', 'first_name', 'last_name', 'username', 'is_verified', 'farm_id', 'is_terms_accepted']


class UserProfileInfoSerializer(serializers.ModelSerializer):
    # is_verified = serializers.BooleanField(read_only=True)
    # farm_id = serializers.SerializerMethodField()

    # def get_farm_id(self, obj):
    #     try:
    #         if Farms.objects.filter(user=obj).exists():
    #             farm = Farms.objects.filter(user=obj).first()
    #             return farm.id
    #         else:
    #             return None
    #     except Farms.DoesNotExist:
    #         return None

    class Meta:
        model = User
        fields = ['id', 'email', 'phone_no', 'first_name', 'last_name', 'username', 'company_name', "user_image",
                  'sic_gst_code', 'pan_no', 'address_one', 'address_two', 'pincode', 'website', 'is_verified', 'is_terms_accepted']
        #userdata()

    def create(self, validated_data):
        image_data = self.context.get('view').request.FILES
        print('cycle create validated data',validated_data)
        print('image_data details',image_data)
        user_instance = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_no=validated_data['phone_no'],
            company_name=validated_data['company_name'],
            sic_gst_code=validated_data['sic_gst_code'],
            pan_no=validated_data['pan_no'],
            address_one=validated_data['address_one'],
            address_two=validated_data['address_two'],
            pincode=validated_data['pincode'],
            website=validated_data['website'],
            email=validated_data['email'],
            user_image = validated_data["user_image"]
        )
        return user_instance

    def update(self, instance, validated_data):
        image_data = self.context.get('view').request.FILES
        print('cycle update validated data',validated_data)
        print('image_data details',image_data)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.sic_gst_code = validated_data.get('sic_gst_code', instance.sic_gst_code)
        instance.pan_no = validated_data.get('pan_no', instance.pan_no)
        instance.address_one = validated_data.get('address_one', instance.address_one)
        instance.address_two = validated_data.get('address_two', instance.address_two)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.website = validated_data.get('website', instance.website)
        instance.email = validated_data.get('email', instance.email)
        instance.user_image = validated_data.get('user_image', instance.user_image)
        instance.save()

        return instance


class RolesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Roles
        fields = "__all__"