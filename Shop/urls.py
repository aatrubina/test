from django.urls import path, include
from django.contrib import admin  # Импортируем admin из django.contrib

from OnlineShop import views  # Импорт из папки OnlineShop


urlpatterns = [
    path('admin/', admin.site.urls),  # URL-шаблон для административной панели Django
    path('', views.home, name='home'),  # Путь URL для главной страницы
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('order/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('payment/create/', views.PaymentCreateView.as_view(), name='payment-create'),
]
