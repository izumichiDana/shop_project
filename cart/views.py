from rest_framework import generics
from django.shortcuts import get_object_or_404
from products.models import  Product
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .helpers import Cart
from .models import *
from .serializers import *


class AddToCart(CreateAPIView):

    """
    Добавление товара в корзину
    """
    def post(self, request, product_id, ):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add_or_update(product)

        return Response({"status": "success"})


class GetCart(APIView):
    """
    Получение товара из корзины
    """

    def get(self, request, format=None):
        cart = Cart(request)
        cart.__iter__()

        product_serial = CartSerializer( many=True, context=cart.cart)
        price = cart.get_total_price()
        order = {
            "quantity": cart.__len__(),
            'line' : cart.get_total_quantity(),
            "total_price": price['price'],
            "discount_price": price['price'] - price['sale'],
            "final_price": price['sale']
            }

        return Response({"Cart": product_serial.data, "Order": order})


class CartRemove(APIView):

    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        cart.remove(product=product)
        return Response({"status": "success"})


class OrderAPIView(CreateAPIView):

    queryset = Byer.objects.all()
    serializer_class = ByerSerializer

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        order = Byer.objects.create(
        name = request.data['name'],
        last_name = request.data['last_name'],
        email = request.data['email'],
        phone_num = request.data['phone_num'],
        country = request.data['country'],
        city = request.data['city']
    )

        price = cart.get_total_price()
        check = Order.objects.create(
            byer=order,
            quantity=cart.__len__(),
            stock=cart.get_total_quantity(),
            price=price['price'],
            sale=price['price'] - price['sale'],
            final_price=price['sale'])


        for key, item in cart.cart.items():
            for id in item['product']:
                print(item)
                image = ProductImage.objects.get(id=int(id))
                print(image)
                old_price = item['old_price']
                price = item['price']
                # count = color
                OrderProduct.objects.create(
                    byer=check,
                    old_price=old_price,
                    price=price,
                    # count=count,
                    image=image.image,
                    color=image.color,
                    name=image.image.name,
                    size_range=image.image.size
                    )
        

        cart.clear()
        return Response({'status': 'success'})





