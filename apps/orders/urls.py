from django.urls import path
from .views import *

urlpatterns = [
    path('', order_list_view, name='order_list'),
    path('<int:pk>/', order_detail_view, name='order_detail'),
    path('<int:pk>/accept/', order_accept_view, name='order_accept'),
    path('<int:pk>/complete/', order_complete_view, name='order_complete'),
    path('<int:pk>/cancel/', order_cancel_view, name='order_cancel'),
]
