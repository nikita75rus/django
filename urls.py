from django.urls import path
from . import views

# Маршруты для приложения core
urlpatterns = [
    # Главная страница - пустой путь означает корень сайта
    path('', views.landing, name='landing'),
    # Страница благодарности
    path('thanks/', views.thanks, name='thanks'),
    # Список всех заявок
    path('orders/', views.orders_list, name='orders_list'),
    # Детальная страница заявки с параметром order_id
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
]