from rest_framework.response import Response
from rest_framework import generics
from .models import Category, Product
from .serializer import CategorySerializer, ProductDetailSerializer, ProductListSerializer, ProductDeleteSerializer


class CategoryCreateView(generics.CreateAPIView):
    ''' Создание категории '''
    serializer_class = CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteView(generics.DestroyAPIView):
    ''' Удаление категории '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        is_use = True
        instance = self.get_object()
        products = Product.objects.all()
        for product in products:
            for cat in product.category.all():
                if cat.pk == instance.pk:
                    is_use = False
                    return Response({'error': 'Категория имеет один или несколько Товаров'})
        if is_use:
            instance.delete()
            instance.save()
            return Response({'complete': 'Удаление прошло успешно'})


class ProductsAllListView(generics.ListAPIView):
    ''' Вернуть список всех товаров '''
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductsListView(generics.ListAPIView):
    ''' Вернуть список активных товаров '''
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductListSerializer


class ProductsDeleteListView(generics.ListAPIView):
    ''' Вернуть список удаленных товаров '''
    queryset = Product.objects.filter(is_deleted=True)
    serializer_class = ProductListSerializer


class ProductDetailView(generics.RetrieveAPIView):
    ''' Возвращение полной информации о товаре '''
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateView(generics.CreateAPIView):
    ''' Создать новый товар '''
    serializer_class = ProductDetailSerializer


class ProductEditView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductDeleteView(generics.UpdateAPIView):
    ''' Помечает товар как удаленный '''
    queryset = Product.objects.all()
    serializer_class = ProductDeleteSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'complete': 'complete'})