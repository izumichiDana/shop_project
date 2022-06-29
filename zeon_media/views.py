from rest_framework.viewsets import ModelViewSet
from .models import * 
from .serializers import *
from rest_framework.pagination import PageNumberPagination
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

class SliderView(ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    http_method_names = ['get']


class CallBackView(generics.ListCreateAPIView):
    queryset = CallBack.objects.all()
    serializer_class = CallBackSerializer

class HelpersView(generics.ListAPIView):
    queryset = HelpImage.objects.all()
    serializer_class = HelpImageSerializer

class OurAdvantagesView(ModelViewSet):
    queryset = OurAdvantages.objects.all()
    serializer_class = OurAdvantagesSerializer
    http_method_names = ['get']

class FuterView(generics.ListAPIView):
    queryset = Futer.objects.all()
    serializer_class = FuterSerializer

class FuterLinkView(generics.ListAPIView):
    queryset = FuterLink.objects.all()
    serializer_class = FuterLinkSerializer