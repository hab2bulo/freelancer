from django.urls import path
from .views import service_list_view, service_create_view, service_detail_view

urlpatterns = [
    path('', service_list_view, name='service_list'),
    path('create/', service_create_view, name='service_create'),
    path('<int:pk>/', service_detail_view, name='service_detail'),
]
