from rest_framework import viewsets
from .serializers import *
from product.models import Product, ProductVariant, ProductVariantPrice, ProductImage


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


class ProductVariantPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductVariantPrice.objects.all()
    serializer_class = ProductVariantPriceSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer



