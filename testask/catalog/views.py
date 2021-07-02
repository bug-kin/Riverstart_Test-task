from rest_framework.response import Response
from rest_framework import generics
from .models import Category, Product
from .serializer import CategorySerializer, ProductDetailSerializer, ProductListSerializer, ProductDeleteSerializer


class ProductsAllListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductListSerializer


class ProductsDeleteListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_deleted=True)
    serializer_class = ProductListSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductEditView(generics.UpdateAPIView):
    serializer_class = ProductDetailSerializer


class ProductDeleteView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'complete': 'complete'})

