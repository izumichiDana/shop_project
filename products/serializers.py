from dataclasses import fields
from rest_framework import serializers
from .models import * 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('slug', )

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        exclude = ('slug', )

class CollectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'name', 'old_price','price', 'sale', 'size', 'favorite', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerialiser(instance.images.all(), many=True, context=self.context).data
        return representation

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'name', 'old_price','price', 'sale', 'size', 'favorite', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerialiser(instance.images.all(), many=True, context=self.context).data
        return representation

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('slug', )

    def validate_name(self, name):
        if Product.objects.filter(slug=name.lower().replace(' ', '-')).exists():
            raise serializers.ValidationError('Product with such name already exists')
        return name

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['collection'] = instance.collection.name
        representation['category'] = instance.category.name
        representation['images'] = ImageSerialiser(instance.images.all(), many=True, context=self.context).data
        return representation

class ImageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
