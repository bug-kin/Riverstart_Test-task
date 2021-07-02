from django.urls import path

from .views import ProductsAllListView,\
    ProductsListView,\
    ProductDetailView, \
    ProductCreateView, \
    ProductDeleteView, \
    ProductsDeleteListView

app_name = 'catalog'

urlpatterns = [
    path('allproducts/', ProductsAllListView.as_view(), name='all-products'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create-product'),
    # path('edit/<int:pk>', ProductEditView.as_view(), name='edit-product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete-product'),
    path('deletedlist/', ProductsDeleteListView.as_view(), name='deleted-list'),
]
