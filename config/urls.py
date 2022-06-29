"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from products.views import *
from zeon_media.views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Zeon',
        default_version='v1',
        description='My API'
    ),
    public=True
)
router = DefaultRouter()

router.register('slider', SliderView)
router.register('top_saled', TopSaledProductView)
router.register('new_product', NewProductView)
router.register('collection', CollectionView)
router.register('our_advantages', OurAdvantagesView)
router.register('products', ProductView)
router.register('favorite', FavoriteProductView)



urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/products/favorite/<int:id>/', favorite),
    path('api/v1/zeon_media/', include('zeon_media.urls')),
    path('api/v1/cart/', include('cart.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
