
from company.models import Company
from rest_framework import serializers


class  CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'