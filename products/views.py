from django.shortcuts import render
from requests import Response
from .models import * 
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

class MyPaginationClass(PageNumberPagination):
    page_size = 8

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CollectionViewSwet(ModelViewSet):
    queryset = Collections.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = MyPaginationClass

class CollectionDetailViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CollectionDetailSerializer
    pagination_class = MyPaginationClass

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(collection_id=kwargs['pk'])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_context(self):
        context = super(CollectionDetailViewSet, self).get_serializer_context()
        context.update({'request':self.request})
        return context

class FavoriteViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = FavoriteSerializer
    pagination_class = MyPaginationClass

    # def list(self, request, *args, **kwargs):
    #     queryset = Product.objects.filter(product_id=kwargs)
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def get_serializer_context(self):
    #     context = super(FavoriteViewSet, self).get_serializer_context()
    #     context.update({'request':self.request})
    #     return context

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class=MyPaginationClass
