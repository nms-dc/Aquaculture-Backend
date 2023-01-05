from attr import fields
from species.models import Species, SpeciesCategory
from rest_framework import serializers


class SpeciesCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpeciesCategory
        fields = '__all__'


class SpeciesSerializer(serializers.ModelSerializer):
    species_cat = SpeciesCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Species
        fields = ['id', 'product_name', 'product_desc', 'image', 'fish_common_name', 'fish_scientific_name', 'fish_ranges',
                  'wikipedia', 'createdAt', 'updatedAt', 'species_cat']
