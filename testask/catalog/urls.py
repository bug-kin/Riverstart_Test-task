from django.urls import path

from .views import ProductEditView, ProductsAllListView, ProductsListView, ProductDetailView, ProductCreateView, \
    ProductCategoriesListView, ProductPriceListView, ProductPublishedListView, \
    ProductDeleteView, ProductNameQueryView, CategoryCreateView, CategoryDeleteView, CategoryListView

app_name = 'catalog'

urlpatterns = [
    # Категории
    path('category/create', CategoryCreateView.as_view()),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view()),
    path('category/', CategoryListView.as_view()),
    # Товары
    path('product/create', ProductCreateView.as_view()),
    path('products/all', ProductsAllListView.as_view()),
    path('products', ProductsListView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('product/edit/<int:pk>', ProductEditView.as_view()),
    path('product/delete/<int:pk>', ProductDeleteView.as_view()),
    path('product/name', ProductNameQueryView.as_view()),
    path('product/price', ProductPriceListView.as_view()),
    path('product/published', ProductPublishedListView.as_view()),
    path('product/categories', ProductCategoriesListView.as_view())
]
