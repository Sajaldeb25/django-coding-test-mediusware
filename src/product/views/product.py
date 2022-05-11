
# from product.models import Variant
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from product.models import Variant, Product, ProductVariant, ProductVariantPrice
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.db.models import Q, Count
import datetime


class CreateProductView(TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

