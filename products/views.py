from rest_framework.response import Response
from .models import * 
from .serializers import *
from rest_framework.decorators import  action
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

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
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 5:
            queryset = Product.objects.filter(collection_id=kwargs['pk']).order_by('-id')[:5]
        else:
            queryset = Product.objects.filter(collection_id=kwargs['pk'])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer =  CollectionDetailSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
        
class NewProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(new_product=True)
    serializer_class = CollectionDetailSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class=MyPaginationClass

    @action(detail=False, methods=['GET'])  #action dostupny tol'ko v ViewSet / router builds path/search/?q=paris
    def search(self, request, pk=None):
        q = request.query_params.get('q')    #request.query_params = request.GET
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(name__icontains=q))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer =  CollectionDetailSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

# class SameProductViewSet(ModelViewSet):
#     """Похожие товары"""
#     queryset = Product.objects.all()
#     serializer_class = CollectionDetailSerializer

#     def list(self, request, *args, **kwargs):
#         if Product.objects.filter(collection_id=kwargs['pk']).count() > 5:
#             queryset = Product.objects.filter(collection_id=kwargs['pk']).order_by('-id')[:5]
#         else:
#             queryset = Product.objects.filter(collection_id=kwargs['pk'])
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)