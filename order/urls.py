from django.urls import path
from order.views import (
    SaveOrder,
    Checkout,
    Orders
)
urlpatterns = [
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('save-order/', SaveOrder.as_view(), name='save-order'),
    path('orders/', Orders.as_view(), name='orders'),       
]