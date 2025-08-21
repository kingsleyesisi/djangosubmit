from django.urls import path
from .views import (
    HomeView,
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    SaleListView, SaleCreateView, SaleUpdateView, SaleDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    
    path('sales/', SaleListView.as_view(), name='sale_list'),
    path('sales/create/', SaleCreateView.as_view(), name='sale_create'),
    path('sales/<int:pk>/update/', SaleUpdateView.as_view(), name='sale_update'),
    path('sales/<int:pk>/delete/', SaleDeleteView.as_view(), name='sale_delete'),
]