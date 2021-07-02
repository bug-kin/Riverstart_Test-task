from django.urls import path

from .views import ProductEditView, ProductsAllListView, ProductsListView, ProductDetailView, ProductCreateView, \
    ProductDeleteView, ProductsDeleteListView, CategoryCreateView, CategoryDeleteView, CategoryListView

app_name = 'catalog'

urlpatterns = [
    # Категории
    path('create-category/', CategoryCreateView.as_view(), name='create-category'),
    path('delete-category/<int:pk>', CategoryDeleteView.as_view(), name='delete-category'),
    path('categories/', CategoryListView.as_view(), name='delete-category'),
    # Товары
    path('create-product/', ProductCreateView.as_view(), name='create-product'),
    path('allproducts/', ProductsAllListView.as_view(), name='all-products'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('edit-product/<int:pk>', ProductEditView.as_view(), name='edit-product'),
    path('delete-product/<int:pk>', ProductDeleteView.as_view(), name='delete-product'),
    path('deletedlist/', ProductsDeleteListView.as_view(), name='deleted-list'),
]
