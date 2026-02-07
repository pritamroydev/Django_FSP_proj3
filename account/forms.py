from django.forms import ModelForm
from .models import Order,Customer

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'


class UpdateOrder(ModelForm):
    class Meta:
        model=Order
        exclude=['customer']


class CustomerFrom(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'