from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'is_deleted']