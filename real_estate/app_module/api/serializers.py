from rest_framework import serializers
from app_module.models import Flat, Builder, Campaign, Category,Lead, ResaleFlat, RentFlat


class BuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Builder
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FlatSerializer(serializers.ModelSerializer):
    builder = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Flat
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        
class ResaleFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResaleFlat
        fields = '__all__'


class RentFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentFlat
        fields = '__all__'

