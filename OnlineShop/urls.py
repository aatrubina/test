from django.contrib import admin
from django.urls import path, include  # Импортируем функцию include для включения URL-шаблонов из других приложений

urlpatterns = [
    path('admin/', admin.site.urls),  # Добавляем URL-шаблон для административной панели Django
    path('', include('OnlineShop.urls')),  # Включаем URL-шаблоны вашего приложения OnlineShop
]
