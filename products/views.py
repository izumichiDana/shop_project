from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import * 
from .serializers import *
from rest_framework.decorators import  action, api_view
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
import random 
from rest_framework.views import APIView

class MyPaginationClass(PageNumberPagination):
    page_size = 8

class PaginationDetail(PageNumberPagination):
    page_size = 12

class NewProductPagination(PageNumberPagination):
    page_size = 5

"""
Глобальная функция рандома
"""
def get_random_objects(massiv, count):
    data = set(massiv.objects.all())
    res = random.sample(data, count)
    return res

class CollectionView(ModelViewSet):
    queryset = Collections.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = MyPaginationClass
    http_method_names = ['get']


class CollectionDetailView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = CollectionDetailSerializer
    pagination_class = PaginationDetail

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(collection_title_id=kwargs['pk'])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# новинки
class NewProductView(ModelViewSet):
    queryset = Product.objects.filter(new_product=True).order_by('-id')[:4]
    serializer_class = CollectionDetailSerializer
    pagination_class=MyPaginationClass
    http_method_names = ['get']


class TopSaledProductView(ModelViewSet):
    queryset = Product.objects.filter(top_saled=True).order_by('-id')[:8]
    serializer_class = CollectionDetailSerializer
    pagination_class=MyPaginationClass
    http_method_names = ['get']


class FavoriteProductView(ModelViewSet):
    queryset = Product.objects.filter(favorites=True).order_by('-id')[:12]
    serializer_class = CollectionDetailSerializer
    pagination_class=MyPaginationClass
    http_method_names = ['get']


    def list(self, request,  *args, **kwargs,):
        queryset = Product.objects.filter(favorites=True)
        serializer = self.get_serializer(queryset, many=True)
        random_collect = get_random_objects(Collections, 5)
        random_colecct_products = []
        products = []
        if not queryset:
            for collection in random_collect:
                random_colecct_products.append({'key': collection.products.all()})
            for product in random_colecct_products:
                products.append(random.choice(product['key']))
            queryset = products[:5]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
def favorite(request, id):
    product = Product.objects.get(id=id)
    if CheckBocks.objects.filter(product=product):
        CheckBocks.objects.get(product=product).delete()
    else:
        CheckBocks.objects.create(product=product)
    serializer = ProductSerializer(product)
    product.favorites = True
    product.save()
    return Response(serializer.data)


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class=MyPaginationClass
    http_method_names = ['get']
    
    
    @action(detail=False, methods=['GET'])  #action dostupny tol'ko v ViewSet / router builds path/search/?q=paris
    def search(self, request,  pk=None,):
        q = request.query_params.get('q')    #request.query_params = request.GET
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(name__icontains=q))
        random_collect = get_random_objects(Collections, 5)
        random_colecct_products = []
        products = []
        if not queryset:
            for collection in random_collect:
                random_colecct_products.append({'key': collection.products.all()})
            for product in random_colecct_products:
                products.append(random.choice(product['key']))
            queryset = products[:5]
        else:
            page = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


"""Похожие товары"""
class SameProductDetailView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = CollectionDetailSerializer
    pagination_class=MyPaginationClass

    def list(self, request,  *args, **kwargs,):
        queryset = Product.objects.filter(collection_title_id=kwargs['pk']).order_by('-id')[:5]
        serializer = self.get_serializer(queryset, many=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
