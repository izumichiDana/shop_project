from rest_framework import serializers
from .models import * 

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        exclude = ('slug', )

class CollectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'name', 'old_price','price', 'sale', 'size', 'favorite', 'collection', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerialiser(instance.images.all(), many=True, context=self.context).data
        representation['collection'] = instance.collection.name
        return representation

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('slug', 'top_saled', 'new_product', 'available', 'created_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['collection'] = instance.collection.name
        representation['favorite'] = instance.favorites.all()
        representation['images'] = ProductImageSerialiser(instance.images.all(), many=True, context=self.context).data
        return representation

class ProductImageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ('product', )