from django.urls import path
from .views import (
    project_list_view,
    project_detail_view,
    project_create_view,
)

urlpatterns = [
    path('', project_list_view, name='project_list'),
    path('create/', project_create_view, name='project_create'),
    path('<int:pk>/', project_detail_view, name='project_detail'),
]
