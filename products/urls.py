from django.urls import path
from . views import *

urlpatterns = [
    path('collection/', CollectionView.as_view()),
    path('collection_detail/<int:pk>/', CollectionDetailView.as_view()),
    path('new_product/', NewProductView.as_view()),
    path('products_list/', ProductView.as_view()),
    path('product_detail/<int:pk>/', SameProductDetailView.as_view()),
]