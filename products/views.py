from rest_framework.response import Response
from .models import * 
from .serializers import *
from rest_framework.decorators import  action
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, generics
import random 

# Глобальная функция рандома
def get_random_objects(massiv, count) -> list :
    # colect = set(Collection.objects.all())
    # prods = set(Product.objects.filter(collect='collection'))
    # some_data = [{colect : prods for collect, prods in }]
    data = set(massiv.objects.all())
    res = [random.sample(data, count)][0]
    return res

class MyPaginationClass(PageNumberPagination):
    page_size = 8

class PaginationDetail(PageNumberPagination):
    page_size = 12

class NewProductPagination(PageNumberPagination):
    page_size = 5

class CollectionView(generics.ListAPIView):
    queryset = Collections.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = MyPaginationClass

class CollectionDetailView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = CollectionDetailSerializer
    pagination_class = PaginationDetail

    def castom(self, request, *args, **kwargs):
        queryset = Product.objects.filter(collection_id=kwargs['pk'])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# новинки
class NewProductView(generics.ListAPIView):
    queryset = Product.objects.filter(new_product=True).order_by('-id')[:5]
    serializer_class = CollectionDetailSerializer
    # pagination_class = NewProductPagination

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class=MyPaginationClass
    
    @action(detail=False, methods=['GET'])  #action dostupny tol'ko v ViewSet / router builds path/search/?q=paris
    def search(self, request, pk=None):
        q = request.query_params.get('q')    #request.query_params = request.GET
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(name__icontains=q))
        if not queryset:
            random_objects = get_random_objects(Product, 5)
            serializer = CollectionDetailSerializer(random_objects, many=True)
            return Response(serializer.data)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CollectionDetailSerializer(random_objects, queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class SameProductDetailView(generics.ListAPIView):
    """Похожие товары"""
    queryset = Product.objects.all()
    serializer_class = CollectionDetailSerializer
    pagination_class=MyPaginationClass

    def castom(self, request, *args, **kwargs):
        queryset = Product.objects.filter(collection_id=kwargs['pk']).order_by('-id')[:5]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
