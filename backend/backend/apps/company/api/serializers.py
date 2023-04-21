from company.models import Company, CompanyFeedType
from rest_framework import serializers
#from company.single_backup import farmdata


class CompanyFeedTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyFeedType
        fields = '__all__'


class CompanySerializers(serializers.ModelSerializer):
    types= serializers.SerializerMethodField()
    #farmdata()
    def get_types(self, obj):
        data = CompanyFeedType.objects.filter(company = obj.id)
        serialize = CompanyFeedTypeSerializers(data, many=True).data
        return serialize
    
    class Meta:
        model = Company
        fields = '__all__'



class getFeedTypeSerializers(serializers.ModelSerializer):
    types= serializers.SerializerMethodField()
    
    def get_types(self, obj):
        data = CompanyFeedType.objects.filter(company = obj.id)
        serialize = CompanyFeedTypeSerializers(data, many=True).data
        return serialize
    
    class Meta:
        model = Company
        fields = ['types']


class CompanyFeedSerializers(serializers.ModelSerializer):
    feeds = serializers.SerializerMethodField()
        
    def get_feeds(self, obj):
        feed_data = Company.objects.all()
        feed_serialize = CompanySerializers(feed_data, many=True).data
        data = []
        for i in feed_serialize:
            company_type = i['company_type']
            if company_type == 'F':
                data.append(i)
        return data        
    
    class Meta:
        model = Company
        fields = ['feeds']


class CompanyProbioticsSerializers(serializers.ModelSerializer):
    feeds = serializers.SerializerMethodField()
        
    def get_feeds(self, obj):
        feed_data = Company.objects.all()
        feed_serialize = CompanySerializers(feed_data, many=True).data
        data = []
        for i in feed_serialize:
            company_type = i['company_type']
            if company_type == 'P':
                data.append(i)
        return data        
    
    class Meta:
        model = Company
        fields = ['feeds']


class CompanySeedsSerializers(serializers.ModelSerializer):
    feeds = serializers.SerializerMethodField()
        
    def get_feeds(self, obj):
        feed_data = Company.objects.all()
        feed_serialize = CompanySerializers(feed_data, many=True).data
        data = []
        for i in feed_serialize:
            company_type = i['company_type']
            if company_type == 'S':
                data.append(i)
        return data        
    
    class Meta:
        model = Company
        fields = ['feeds']


class CompanyFeedProSerializers(serializers.ModelSerializer):
    feeds = serializers.SerializerMethodField()
        
    def get_feeds(self, obj):
        feed_data = Company.objects.all()
        feed_serialize = CompanySerializers(feed_data, many=True).data
        data = []
        for i in feed_serialize:
            company_type = i['company_type']
            if company_type == 'F/P':
                data.append(i)
        return data        
    
    class Meta:
        model = Company
        fields = ['feeds']



