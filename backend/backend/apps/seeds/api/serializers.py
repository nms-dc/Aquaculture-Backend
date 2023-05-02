
from rest_framework import serializers
#from feeds.single_backup import farmdata
from seeds.models import SeedPlStage, SeedImage, Seeds, Species
from company.models import Company


class SeedImageserializers(serializers.ModelSerializer):
    
    class Meta:
        model = SeedImage
        fields = "__all__"


class Seedserializers(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    def get_company_name(self,obj):
        company_data = Company.objects.filter(company_name = obj.seed_company_id).values()
        return company_data[0]["company_name"]

    
    class Meta:
        model = Seeds
        fields = "__all__"

    def create(self, validated_data):
        image_datas = self.context.get('view').request.FILES
        print('measurement create validated data',validated_data)
        print('image_data details',image_datas)
        measurement_instance = Seeds.objects.create(
            lot_number=validated_data['lot_number'],
            date_received=validated_data['date_received'],
            number_of_eggs=validated_data['number_of_eggs'],
            date_sold=validated_data['date_sold'],
            date_hatched=validated_data['date_hatched'],
            qr_code_id=validated_data['qr_code_id'],
            quality=validated_data['quality'],
            weight=validated_data['weight'],
            price=validated_data['price'],
            farm=validated_data['farm'],
            seed_company_id=validated_data['seed_company_id'],
            species=validated_data['species'],
            species_pl_stage=validated_data['species_pl_stage'],
            created_by=validated_data['created_by']
            )

        for data in image_datas.getlist('feeds_images'):
            name = data.name
            SeedImage.objects.create(fish_ids=measurement_instance, user=name, image=data, created_by=validated_data['created_by'])

        return measurement_instance

    def update(self, instance, validated_data):
        image_datas = self.context.get('view').request.FILES
        data = self.context['request'].data.get('measure_images_id', None)
        int_image_id = []
        if data:
            trim_image_id = data.replace('[', '').replace(']', '').replace(" ", "").split(',')
            for id in trim_image_id:
                int_image_id.append(int(id))

        print('measurement update validated data',validated_data)
        print('image_data details',image_datas)
        print('feeds_image_id',int_image_id)
        instance.lot_number = validated_data.get('lot_number', instance.lot_number)
        instance.date_received = validated_data.get('date_received', instance.date_received)
        instance.number_of_eggs = validated_data.get('number_of_eggs', instance.number_of_eggs)
        instance.date_sold = validated_data.get('date_sold', instance.date_sold)
        instance.date_hatched = validated_data.get('date_hatched', instance.date_hatched)
        instance.qr_code_id = validated_data.get('qr_code_id', instance.qr_code_id)
        instance.quality = validated_data.get('quality', instance.quality)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.price = validated_data.get('price', instance.price)
        instance.farm = validated_data.get('farm', instance.farm)
        instance.seed_company_id = validated_data.get('seed_company_id', instance.seed_company_id)
        instance.species = validated_data.get('species', instance.species)
        instance.species_pl_stage = validated_data.get('species_pl_stage', instance.species_pl_stage)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.save()

        feedimage_with_same_profile_instance = SeedImage.objects.filter(fish_ids=instance.pk).values_list('id', flat=True)

        if len(int_image_id) != 0:
            for delete_id in feedimage_with_same_profile_instance:
                if delete_id in int_image_id:
                    SeedImage.objects.filter(pk=delete_id).delete()
        if len(image_datas.getlist('seed_images')) != 0:
            for image_data in image_datas.getlist('feeds_images'):
                name = image_data.name
                SeedImage.objects.create(fish_ids=instance, image=image_data, updated_by = validated_data.get('updated_by', instance.updated_by))
        return instance

# class FeedLotsserializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = FeedLots
#         fields = "__all__"


# class FeedTypeserializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = FeedType
#         fields = "__all__"

