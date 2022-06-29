from rest_framework import serializers
from .helpers import * 
from products.models import ProductImage, Product
from .models import *
from .models  import Byer

class ByerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Byer
        exclude = ('created_at', )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для проуктов корзины
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'sale', 'price', 'stock']


class CartSerializer(serializers.ModelSerializer):
    """
    Сериализатор для самой корзины
    """
    def get_product(self):
        serializer = CartProductSerializer(context=self.context)
        return serializer.data


    product = serializers.SerializerMethodField('get_product')

    class Meta:
        model = Product
        fields = ['quantity', 'image', 'color', 'product']


class Product_to_OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для заказанных продуктов
    """
    class Meta:
        model = OrderProduct
        fields = '__all__'


class Order_checkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для чека заказа
    """
    product = Product_to_OrderSerializer(many=True, )

    class Meta:
        model = Order
        fields = ['id',
                  'product',
                  'quantity_line',
                  'quantity',
                  'price',
                  'sale',
                  'final_price']
















                  