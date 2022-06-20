
from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('news/', NewsViewSet.as_view()),
    path('help/', HelpersView.as_view()),
    path('public_offert/', PublicOffertView.as_view()),
    path('about_us/', AboutUsView.as_view()),
    path('call_back/', CallBackView.as_view()),
    path('slider/', SliderView.as_view()),

]