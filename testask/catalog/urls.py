from django.urls import path

from .views import ProductEditView, ProductsAllListView, ProductsListView, ProductDetailView, ProductCreateView, ProductCategoriesListView, \
    ProductDeleteView, ProductsDeleteListView, CategoryCreateView, CategoryDeleteView, CategoryListView

app_name = 'catalog'

urlpatterns = [
    # Категории
    path('category/create', CategoryCreateView.as_view()),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view()),
    path('category/', CategoryListView.as_view()),
    # Товары
    path('product/create', ProductCreateView.as_view()),
    path('products/all', ProductsAllListView.as_view()),
    path('', ProductsListView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('product/edit/<int:pk>', ProductEditView.as_view()),
    path('product/delete/<int:pk>', ProductDeleteView.as_view()),
    path('product/deleted', ProductsDeleteListView.as_view()),
    path('product/categories', ProductCategoriesListView.as_view())
]
