from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),   
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product')
    ]
