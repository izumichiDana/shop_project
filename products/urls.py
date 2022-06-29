from django.urls import path
from . views import *

urlpatterns = [
    path('collection_detail/<int:pk>/', CollectionDetailView.as_view()),
    path('same_products/<int:pk>/', SameProductDetailView.as_view()),
    # path('favorite/add/<int:pk>', Favorite_ADD.as_view()),


]