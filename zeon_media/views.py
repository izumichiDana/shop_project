from rest_framework.viewsets import ModelViewSet
from .models import * 
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework import generics

class MyPaginationClass(PageNumberPagination):
    page_size = 8

class NewsViewSet(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class=MyPaginationClass

class PublicOffertView(generics.ListAPIView):
    queryset = PublicOffert.objects.all()
    serializer_class = PublicOffertSerializer

class AboutUsView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class SliderView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class CallBackView(generics.ListCreateAPIView):
    queryset = CallBack.objects.all()
    serializer_class = CallBackSerializer

class HelpersView(generics.ListAPIView):
    queryset = HelpImage.objects.all()
    serializer_class = HelpImageSerializer

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['action'] = self.action
    #     return context