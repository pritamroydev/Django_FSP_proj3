from django.urls import path
from .import views

urlpatterns = [
    
    path('login',views.loginpage, name='login'),  
    path('register',views.registerpage, name='register'),
    path('logout',views.logoutpage,name='logout'),
    path('',views.Home, name='home'),
    path('product', views.Prod, name='product'),
    path('customer/<int:pk_test>', views.Cust, name='customer'),
    path('cust_list',views.Customer_list,name='customer_list'),
    path('create_order',views.create_order,name='create_order'),
    path('place_order/<str:pk>/',views.place_order,name='place_order'),
    path('update_order/<str:pk>/',views.update_order,name='update_order'),
    path('delete_order/<str:pk>',views.delete_order,name='delete_order'),
    path('order_list',views.order_list,name='order_list'),
    path('create_customer/',views.create_customer,name='create_customer'),
    path('update_customer/<str:pk>/',views.update_customer,name='update_customer'),
    path('delete_customer/<str:pk>/',views.deletecustomer,name='delete_customer'),
    path('add_product',views.add_product,name='add_product'),    
    path('update_product/<str:pk>/',views.update_product,name='update_product'),
    path('delete_product/<str:pk>/',views.deleteproduct,name="delete_product"),
    path('tag_list',views.tag_list,name='tag_list'),
    path('import_csv',views.import_tag_csv,name='import_csv'),
    


    
]