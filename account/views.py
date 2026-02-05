from django.shortcuts import render
from .models import Product,Customer,Order,Tag

# Create your views here.
def Home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_order=orders.count()
    total_customer=customers.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    out_for_delivery=orders.filter(status='Out for Delivery').count()
    context = {
        'total_customer': total_customer,
        'total_order': total_order,
        'delivered': delivered,
        'pending': pending,
        'out_for_delivery': out_for_delivery,
        'customers': customers,
        'orders': orders
    }

    return render(request, 'account/dashboard.html',context)




def Prod(request):
    product=Product.objects.all()
    context={'product':product}
    return render(request, 'account/product.html',context)

def Cust(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()
    context={
        'customer': customer,
        'orders':orders,
        'order_count':order_count
    }
    return render(request, 'account/customer.html',context)


def Customer_list(request):
    customer=Customer.objects.all()
    context={'customer':customer}
    return render(request, 'account/customer_list.html', context)
