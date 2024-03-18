from rest_framework import generics
from .models import Order, Payment, Product
from .serializers import OrderSerializer, PaymentSerializer, ProductSerializer

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin_base.html')

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        products_data = request.data.pop('products', [])
        total_amount = sum(product['price'] for product in products_data)
        request.data['total_amount'] = total_amount
        return super().create(request, *args, **kwargs)

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
