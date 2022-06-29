from rest_framework import serializers
from .models import * 

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collections
        fields = '__all__'


class CollectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'name', 'old_price','price', 'sale', 'size', 'favorite', 'collection_title', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerialiser(instance.images.all(), many=True, context=self.context).data
        representation['collection_title'] = instance.collection_title.title
        return representation

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('top_saled', 'new_product', 'created_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['collection_title'] = instance.collection_title.title
        representation['favorites'] = instance.favorite.all().count()
        representation['images'] = ProductImageSerialiser(instance.images.all(), many=True, context=self.context).data
        return representation

class ProductImageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ('product', )