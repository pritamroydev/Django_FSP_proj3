from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('product', views.Prod, name='product'),
    path('customer/<int:pk_test>', views.Cust, name='customer'),
    path('cust_list',views.Customer_list,name='customer_list'),
    path('create_order',views.create_order,name='create_order'),
    path('update_order/<str:pk>/',views.update_order,name='update_order'),
    path('delete_order/<str:pk>',views.delete_order,name='delete_order'),
    path('order_list',views.order_list,name='order_list'),
    path('create_customer',views.create_customer,name='create_customer'),
    

    
]
