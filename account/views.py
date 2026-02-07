from django.shortcuts import render, redirect
from .models import Product,Customer,Order,Tag
from .forms import OrderForm, UpdateOrder, CustomerFrom, ProductForm

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



def order_list(request):
    order=Order.objects.all()
    return render(request, 'account/order_list.html', {'order':order})





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


# ------------ Added functionality of creating order after clicking in button -------------------

def create_order(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'account/order_form.html',context)



# ------------ Added functionality of updating order after clicking in button without changing the name option-------------------

def update_order(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        form=UpdateOrder(request.POST, instance=order)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.customer=order.customer    #keep original customer
            instance.save()
            return redirect('/')
    else:
        form=UpdateOrder(instance=order)

    context={'form':form, 'order':order, 'customer_name':order.customer.name}
    return render(request, 'account/update_order.html',context)




# ------------ functionality for updating order after clicking in button with changing the name option-------------------

# def update_order(request, pk):
#     order=Order.objects.get(id=pk)
#     form=UpdateOrder(instance=order)


#     if request.method=='POST':
#         form=UpdateOrder(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context={'form':form}
#     return render(request, 'account/order_form.html',context)


# ------------ Added functionality of deleting order after clicking in button without changing the name option-------------------

def delete_order(request, pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'account/delete.html', context)
    


# ------------ Added functionality of creating customer after clicking in button without changing the name option-------------------

def create_customer(request):
    form=CustomerFrom()
    if request.method=="POST":
        form=CustomerFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'account/create_customer.html',context)


def update_customer(request,pk):
    customer=Customer.objects.get(id=pk)
    form=CustomerFrom(instance=customer)
    #form=CustomerForm(instance=customer)

    if request.method=="POST":
        form=CustomerFrom(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'account/create_customer.html', context)


def deleteorder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request,'account/delete.html',context) 

#deleting customer 7-2
def deletecustomer(request,pk):
    customer=Customer.objects.get(id=pk)
    if request.method=="POST":
        customer.delete()
        return redirect('/')
    context={'item':customer}
    return render(request,'account/delete_customer.html',context)


def add_product(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    context={'form':form}
    return render(request, 'account/add_product.html',context)



def update_product(request,pk):
    product=Product.objects.get(id=pk)
    form=ProductForm(instance=product)
    if request.method=='POST':
        form=ProductForm(request.POST , instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')
    context={'form':form}
    return render(request, 'account/add_product.html', context)

def deleteproduct(request,pk):
    product=Product.objects.get(id=pk)
    if request.method=="POST":
        product.delete()
        return redirect('product')
    context={'product':product}
    return render(request,'account/delete_product.html',context)
