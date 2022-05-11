from rest_framework import routers
from product.viewsets import ProductViewSet, ProductVariantViewSet, ProductVariantPriceViewSet, ProductImageViewSet
router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product_variant', ProductVariantViewSet)
router.register(r'product_variant_price', ProductVariantPriceViewSet)
router.register(r'product_image', ProductImageViewSet)

