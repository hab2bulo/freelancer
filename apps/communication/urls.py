from django.urls import path
from .views import order_chat_view

urlpatterns = [
    path('order/<int:order_id>/', order_chat_view, name='order_chat'),
]
