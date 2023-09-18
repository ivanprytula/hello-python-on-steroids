from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from apps.products.api.serializers import ProductSerializer
from apps.products.models import Product


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ("id", "title")
