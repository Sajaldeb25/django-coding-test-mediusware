from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView, CreateProductAPIView, ProductView, ProductEditView
from product.views.variant import VariantView, VariantCreateView, VariantEditView, VariantDeleteView

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),
    path('variant/<int:id>/delete', VariantDeleteView.as_view(), name='delete.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('create-api/', CreateProductAPIView.as_view(), name='create.product.api'),
    path('list/', ProductView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),
    path('edit/<int:id>/', ProductEditView.as_view(), name='edit.product'),

]



