from rest_framework import serializers
from farms.models import Farms, FarmCertification,FarmImage



class FarmImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmImage
        fields = '__all__'

class FarmCertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmCertification
        fields = '__all__'        



class farmSerializer(serializers.ModelSerializer):
    image = FarmImageSerializer(many= True)
    certificate = FarmCertificationSerializer(many= True)

    class Meta:
        model = Farms
        fields = '__all__'
        
    
    def create(self, validated_data):
        certify = validated_data.pop('certificate')
        Farm_instance = Farms.objects.create(**validated_data)
        for data in certify:
            FarmCertification.objects.create(user=Farm_instance,**data)
        return Farm_instance