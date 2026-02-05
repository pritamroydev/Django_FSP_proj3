from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('product', views.Prod, name='product'),
    path('customer/<int:pk_test>', views.Cust, name='customer'),
    path('cust_list',views.Customer_list,name='customer_list'),
    

    
]
